class JsonUtils:
  def initJson(self, file_path):
    with open(file_path, 'r') as myfile:
      return myfile.read()
