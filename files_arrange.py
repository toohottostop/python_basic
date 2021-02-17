import os, time, shutil, zipfile


class Arrange:

    def __init__(self, file_name, path_in, path_out):
        self.file_name = file_name
        self.path_in = os.path.normpath(path_in)
        self.path_out = os.path.normpath(path_out)

    def arrange(self, dir_out_name):
        self.make_out_dir(dir_out_name)
        self.walk_and_copy()

    def make_out_dir(self, dir_out_name):
        if not os.path.isdir(dir_out_name):
            os.mkdir(dir_out_name)
        self.path_out = os.path.normpath(os.path.join(self.path_out, dir_out_name))

    def walk_and_copy(self):
        for root, dirs, files in os.walk(self.path_in):
            for file in files:
                path_to_in_file = os.path.join(root, file)
                time_of_file = time.gmtime(os.path.getmtime(path_to_in_file))
                year, month = time_of_file[0], time_of_file[1]
                out_dir_path_year = os.path.join(self.path_out, str(year))
                out_dir_path_month = os.path.join(out_dir_path_year, str(month))
                if not os.path.exists(out_dir_path_month):
                    os.makedirs(out_dir_path_month)
                    os.makedirs(out_dir_path_month)
                shutil.copy2(path_to_in_file, out_dir_path_month)


class ArrangeZipFile(Arrange):

    def walk_and_copy(self):
        with zipfile.ZipFile(self.file_name) as zip_file:
            for file in zip_file.namelist():
                filename = os.path.basename(file)
                if not filename:
                    continue
                file_year, file_month = zip_file.getinfo(file).date_time[0], zip_file.getinfo(file).date_time[1]
                out_dir_path_year = os.path.join(self.path_out, str(file_year))
                out_dir_path_month = os.path.join(out_dir_path_year, str(file_month))
                if not os.path.exists(out_dir_path_month):
                    os.makedirs(out_dir_path_month)
                source = zip_file.open(file)
                target = open(os.path.join(out_dir_path_month, filename), "wb")
                with source, target:
                    shutil.copyfileobj(source, target)


arrange = Arrange(file_name='icons',
                  path_in='files/icons',
                  path_out='files')
arrange.arrange(dir_out_name='icons_by_year')

# arrange_zip = ArrangeZipFile(file_name='icons.zip',
#                      path_in='files/icons.zip',
#                      path_out='files')
# arrange_zip.arrange(dir_out_name='icons_by_year')
