import hashlib
import os

def hash_file(filepath, algorithm='sha256'):
    """Generate hash of a file using the specified algorithm."""
    if not os.path.isfile(filepath):
        print("File not found.")
        return None

    hash_func = getattr(hashlib, algorithm)()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def save_hash(filepath, hash_value):
    """Save the hash to a .hash file."""
    hash_file_path = filepath + '.hash'
    with open(hash_file_path, 'w') as f:
        f.write(hash_value)
    print(f"Hash saved to {hash_file_path}")

def verify_file(filepath, algorithm='sha256'):
    """Verify file integrity by comparing current hash with saved hash."""
    current_hash = hash_file(filepath, algorithm)
    hash_file_path = filepath + '.hash'

    if not os.path.isfile(hash_file_path):
        print("No saved hash found for comparison.")
        return

    with open(hash_file_path, 'r') as f:
        saved_hash = f.read().strip()

    if current_hash == saved_hash:
        print("✅ File integrity verified. No changes detected.")
    else:
        print("⚠️ File integrity compromised! Hash mismatch.")

def main():
    print("=== File Integrity Verifier ===")
    print("1. Generate and save hash")
    print("2. Verify file integrity")
    choice = input("Choose an option (1/2): ").strip()

    filepath = input("Enter the full path to the file: ").strip()
    algorithm = input("Choose hash algorithm (md5, sha1, sha256): ").strip().lower()

    if algorithm not in hashlib.algorithms_available:
        print("Unsupported hash algorithm.")
        return

    if choice == '1':
        hash_value = hash_file(filepath, algorithm)
        if hash_value:
            print(f"Hash ({algorithm}): {hash_value}")
            save_hash(filepath, hash_value)
    elif choice == '2':
        verify_file(filepath, algorithm)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
