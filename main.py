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
        print(f'Found {len(candidates)} subdirectory candidate(s): {", ".join(directory for directory in candidates)}.')
        return candidates

    def zip_directories(self, directories: list):
        """Individually zip each directory's "Items" folder."""
        for parent_directory in directories:
            for item_directory, item_subdirectories, item_files in walk(path.join(self.origin_path,
                                                                                  parent_directory,
                                                                                  self.subdir_target)):
                new_zip = ZipFile(parent_directory + '.zip', 'w')
                for file in item_files:
                    new_zip.write(path.join(item_directory, file))
                new_zip.close()

    def convert_to_zips(self):
        """Find all KWS folders and zip each one."""
        self.zip_directories(self.get_subdir_candidates())


if __name__ == '__main__':
    exporter = NuixExportZipper()
    exporter.convert_to_zips()
