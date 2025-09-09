from PIL import Image


def stroke(image: Image.Image, strokeColor="#000000", backgroundColor="#00000000") -> Image.Image:
  """
  描边

  :param image:
  :param strokeColor: 描边颜色
  :param backgroundColor: 主观认为的背景颜色
  :return:
  """
  # TODO