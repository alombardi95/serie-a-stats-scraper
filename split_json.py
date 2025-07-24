#!/usr/bin/env python3
"""
Script to split JSON node children into separate files.
Usage: python split_json.py <input_file.json>
"""

import json
import sys
import os
from typing import Any, Dict, List


def load_json(file_path: str) -> Dict[str, Any]:
    """Load JSON from file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{file_path}': {e}")
        sys.exit(1)


def select_node(data: Dict[str, Any]) -> str:
    """Let user select a node from the JSON structure."""
    print("\nAvailable top-level nodes:")
    nodes = list(data.keys())
    
    for i, node in enumerate(nodes, 1):
        node_type = type(data[node]).__name__
        if isinstance(data[node], list):
            node_type += f" ({len(data[node])} items)"
        print(f"{i}. {node} ({node_type})")
    
    while True:
        try:
            choice = input("\nSelect node number to split: ").strip()
            if not choice:
                print("Please enter a valid number.")
                continue
            
            idx = int(choice) - 1
            if 0 <= idx < len(nodes):
                selected = nodes[idx]
                
                # Check if selected node has children (list or dict)
                if not isinstance(data[selected], (list, dict)):
                    print(f"Error: '{selected}' is not a list or dict, cannot split.")
                    continue
                    
                return selected
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            sys.exit(0)


def get_children(data: Dict[str, Any], node_name: str) -> List[Any]:
    """Get children of the selected node."""
    node_data = data[node_name]
    
    if isinstance(node_data, list):
        return node_data
    elif isinstance(node_data, dict):
        # Convert dict to list of key-value pairs
        return [{"key": k, "value": v} for k, v in node_data.items()]
    else:
        return []


def get_key_value_for_filename(obj: Any) -> str:
    """Extract a meaningful key value for filename from JSON object."""
    if isinstance(obj, dict):
        # Try common key names
        for key in ['name', 'id', 'title', 'key', 'label', 'slug']:
            if key in obj and isinstance(obj[key], (str, int, float)):
                value = str(obj[key])
                # Sanitize filename
                value = "".join(c for c in value if c.isalnum() or c in (' ', '-', '_')).strip()
                return value[:50]  # Limit length
    
    # Fallback to index
    return None


def split_and_save(children: List[Any], parent_name: str, output_dir: str = ".") -> None:
    """Split children into separate files."""
    if not children:
        print(f"No children found in '{parent_name}'.")
        return
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Splitting {len(children)} children from '{parent_name}'...")
    
    for i, child in enumerate(children, 1):
        key_value = get_key_value_for_filename(child)
        
        if key_value:
            filename = f"{parent_name}_{key_value}_{i:03d}.json"
        else:
            filename = f"{parent_name}_{i:03d}.json"
        
        file_path = os.path.join(output_dir, filename)
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(child, f, indent=2, ensure_ascii=False)
            print(f"Created: {file_path}")
        except Exception as e:
            print(f"Error creating {file_path}: {e}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python split_json.py <input_file.json>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Load JSON data
    data = load_json(input_file)
    
    # Select node to split
    selected_node = select_node(data)
    
    # Get children
    children = get_children(data, selected_node)
    
    # Split and save
    output_directory = input(f"\nEnter output directory (default: current directory): ").strip()
    if not output_directory:
        output_directory = "."
    
    split_and_save(children, selected_node, output_directory)
    
    print(f"\n✅ Successfully split {len(children)} files into '{output_directory}'")


if __name__ == "__main__":
    main()