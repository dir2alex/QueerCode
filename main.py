# Hello simo!
# I love you!!!!!!!!!1 <33333333333333333333333333

import qrcode
import qrcode.image.svg

factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("Hello World!", image_factory=factory)
svg_img.save("myqr.svg")