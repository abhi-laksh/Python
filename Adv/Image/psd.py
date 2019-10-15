from psd_tools import PSDImage, compose

psd = PSDImage.load('sample.psd')
# psd.print_tree()
txt=psd.layers[0]
layr= compose(txt)
layr.text="Abhishek"
print(layr.text)
layr.save()


