from . import generator
import os

MD5 = generator.HASH_MD5
SHA1 = generator.HASH_SHA1
SHA224 = generator.HASH_SHA224
SHA256 = generator.HASH_SHA256
SHA384 = generator.HASH_SHA384
SHA512 = generator.HASH_SHA512


class Avatar:
    DEFAULT_OUTPUT_PATH = os.path.join(os.getcwd(), "output/")
    DEFAULT_FILENAME = "pagan"
    DEFAULT_EXTENSION = "png"
    ALLOWED_EXTENSIONS = ["bmp", "gif", "png", "tiff"]
    DEFAULT_HASHFUN = generator.HASH_MD5

    def __init__(self, inpt, hashfun=DEFAULT_HASHFUN):
        """Initialize the avatar and creates the image."""
        self.img = self.__create_image(inpt, hashfun)

    def __create_image(self, inpt, hashfun):
        """Creates the avatar based on the input and
        the chosen hash function."""
        if hashfun not in generator.HASHES.keys():
            print(
                "Unknown or unsupported hash function. Using default: %s"
                % self.DEFAULT_HASHFUN
            )
            algo = self.DEFAULT_HASHFUN
        else:
            algo = hashfun
        return generator.generate(inpt, algo)

    def show(self):
        """Shows a preview of the avatar in an external
        image viewer."""
        self.img.show()

    def change(self, inpt, hashfun=DEFAULT_HASHFUN):
        """Change the avatar by providing a new input.
        Uses the standard hash function if no one is given."""
        self.img = self.__create_image(inpt, hashfun)

    def save(
        self,
        path=DEFAULT_OUTPUT_PATH,
        filename=DEFAULT_FILENAME,
        extension=DEFAULT_EXTENSION,
    ):
        """Saves a avatar under the given output path to
        a given filename. The file ending ".png" is appended
        automatically. If the path does not exist, it will be
        created. When no parameters are omitted, a default path
        and/or filename will be used."""
        if extension not in self.ALLOWED_EXTENSIONS:
            raise Exception(
                'Extension "%s" is not supported. Supported extensions are: %s'
                % (extension, ", ".join(self.ALLOWED_EXTENSIONS))
            )
        if not os.path.exists(path):
            os.makedirs(path)
        if extension.startswith("."):
            extension = extension[1:]
        if filename[-len(extension) :] == extension:
            filename = filename[: -len(extension) - 1]
        filepath = "%s%s.%s" % (path, filename, extension)
        filepath = os.path.join(path, "%s.%s" % (filename, extension))
        self.img.save(filepath, extension.upper())
