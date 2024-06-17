import os

from app.data.utils.files_management import generate_file, read_file

def test_generate_file(tmpdir):
    file_name = "test_file"
    file_extension = ".txt"
    file_content = "This is a test."

    # Generate file in the temporary directory
    file_path = tmpdir.join(file_name + file_extension)
    generate_file(str(file_path), "", file_content)

    # Verify the file was created and contains the correct content
    assert os.path.exists(file_path)
    with open(file_path, 'r', encoding="utf-8") as file:
        assert file.read() == file_content

def test_read_file(tmpdir):
    file_name = "test_file"
    file_extension = ".txt"
    file_content = "This is a test."

    # Create a file in the temporary directory
    file_path = tmpdir.join(file_name + file_extension)
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(file_content)

    # Read the file using the function and verify the content
    assert read_file(str(file_path), "") == file_content