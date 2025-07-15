from load_image import ft_load
from pimp_image import ft_red, ft_blue, ft_green, ft_invert, ft_gray

array = ft_load('landscape.jpg')

ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_gray(array)

print(ft_invert.__doc__)