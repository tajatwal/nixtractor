from os import getcwd, makedirs, path, walk
from zipfile import ZipFile


class NuixExportZipper(object):
    """Zip the "Items" subdirectory of each file in the current directory.

    Arguments:
        origin_path (str, optional): Path to the directories to be zipped.
            - Defaults to the current working directory.
        subdir_target (str, optional): Name of the subdirectory to look for in each directory.
            - Defaults to "Items."
        output_dir (str, optional): Path to the directory where the zipped files should be stored.
        - Defaults to "output."
    """
    def __init__(self, origin_path='.', subdir_target: str = 'Items', output_dir: str = 'output'):
        self.origin_path = getcwd() if origin_path == '.' else origin_path
        self.subdir_target = subdir_target
        self.output_dir = output_dir

    def get_subdir_candidates(self):
        """Find all subdirectories that contain an "Items" subdirectory."""
        candidates = list()
        # Get a list of top-level subdirectories in the provided file.
        for parent_directory in next(walk(self.origin_path))[1]:
            # Return the parent directory's name if it has an "Items" folder.
            if self.subdir_target in next(walk(path.join(self.origin_path, parent_directory)))[1]:
                candidates.append(parent_directory)
        return candidates

    def zip_directories(directories: list):
        """Zip the each directory individually."""
        zip_file_path = path.join(parent_directory + '.zip')
        target_directory = path.join(origin_path, parent_directory, subdir_target)
        print(f'Target directory: {target_directory}')
        # if not path.exists(zip_file_path):
        #     makedirs(zip_file_path)
        export_items(origin_path=target_directory,
                     # Name the output file after the subdirectory's parent directory.
                     out_file_handle=ZipFile(outfile)),
        # elif out_file_handle:
        #     with open(zip_file_path, 'w') as outfile:
        #         for directory_name, subdirectories, files in walk(origin_path):
        #             for file in files:
        #                 outfile.write(path.join(directory_name, file))
            # Ensure that there's a directory to put the zipped files into.
            # if not path.exists(output_dir):
            #     makedirs(output_dir)

    def convert_to_zips(self):
        """Find all KWS folders and zip each one."""
        print(self.get_subdir_candidates())


if __name__ == '__main__':
    export_items()
