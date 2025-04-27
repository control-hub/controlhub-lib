import json
import os

def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """
    Merges two dictionaries into one. If there are duplicate keys, the values from dict2 will overwrite those in dict1 except if values are dictionaries, then they will be merged recursively.
    
    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.
    
    Returns:
        dict: A new dictionary containing the merged data.
    """
    merged = dict1.copy()
    
    for key, value in dict2.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = merge_dicts(merged[key], value)
        else:
            merged[key] = value
    
    return merged

class JSONFile:
    def __init__(self, file_path: str):
        """
        Initializes the JSONFile class with the specified file path.
        
        Args:
            file_path (str): Path to the JSON file.
        """
        self.file_path = file_path
        
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump({}, f, ensure_ascii=True, indent=4)

    def get(self) -> dict:
        """
        Reads data from a JSON file and returns it as a dictionary.
        
        Returns:
            dict: Data read from the JSON file.
        """
        with open(self.file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
                with open(self.file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=True, indent=4)
            
        return data

    def merge(self, data: dict) -> None:
        """
        Changes the data in the JSON file to the provided data. (Like append, it does not override everything)
        
        Args:
            data (dict): Data to append to the JSON file.
        """
        current_data = self.get()
        
        with open(self.file_path, 'w', encoding='utf-8') as f:        
            merged_data = merge_dicts(current_data, data)
            json.dump(merged_data, f, ensure_ascii=True, indent=4)
        
        return merged_data

    def set(self, data: dict) -> None:
        """
        Sets the data in the JSON file to the provided data. (Absolutely overrides everything)
        
        Args:
            data (dict): Data to set in the JSON file.
        """
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=True, indent=4)
    
    def __getitem__(self, key):
        """
        Allows access to the JSON data using dictionary-like syntax.
        
        Args:
            key: The key to access in the JSON data.
        
        Returns:
            The value associated with the key in the JSON data.
        """
        return self.get()[key]

    def __setitem__(self, key, value):
        """
        Allows setting a value in the JSON data using dictionary-like syntax.
        
        Args:
            key: The key to set in the JSON data.
            value: The value to set for the key.
        """
        
        data = self.get()
        data[key] = value
        self.set(data)

    def __delitem__(self, key):
        """
        Allows deleting a key from the JSON data using dictionary-like syntax.
        
        Args:
            key: The key to delete from the JSON data.
        """
        
        data = self.get()
        del data[key]
        self.set(data)

    def __iter__(self):
        """
        Allows iteration over the keys in the JSON data.
        
        Returns:
            An iterator over the keys in the JSON data.
        """
        
        return iter(self.get())
    
    def __len__(self):
        """
        Returns the number of keys in the JSON data.
        
        Returns:
            int: The number of keys in the JSON data.
        """
        
        return len(self.get())

    def __contains__(self, key):
        """
        Checks if a key is in the JSON data.
        
        Args:
            key: The key to check for in the JSON data.
        
        Returns:
            bool: True if the key is in the JSON data, False otherwise.
        """
        
        return key in self.get()

    def __str__(self):
        """
        Returns a string representation of the JSON data.
        
        Returns:
            str: A string representation of the JSON data.
        """
        
        return json.dumps(self.get(), ensure_ascii=True, indent=4)

    def __repr__(self):
        """
        Returns a string representation of the JSONFile object.
        
        Returns:
            str: A string representation of the JSONFile object.
        """
        
        return f"JSONFile({self.file_path})"
    
data = JSONFile('data.json')


# === Tests ===

if __name__ == "__main__":
    data.set({})
    
    data.set({"key": "value"})
    assert data.get() == {'key': 'value'}
    
    data["key"] = "new_value"
    assert data.get() == {'key': 'new_value'}
    
    del data["key"]
    assert data.get() == {}
    
    assert len(data) == 0
        
    assert "key" not in data
    
    assert str(data) == "{}"
    
    assert repr(data) == "JSONFile(data.json)"
    
    data.set({"key": "value", "another_key": {"a": "b"}})
    assert data.get() == {'key': 'value', 'another_key': {'a': 'b'}}
    
    data.merge({"another_key": {"b": "new_value"}})
    assert data.get() == {'key': 'value', 'another_key': {'a': 'b', 'b': 'new_value'}}
    
    assert len(data["another_key"]) == 2
    
    print("All tests passed!")
