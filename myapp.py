from bokeh.plotting import figure, show, output_file, curdoc
from bokeh.tile_providers import get_provider, Vendors

output_file("tile.html")

tile_provider = get_provider(Vendors.ESRI_IMAGERY)

# range bounds supplied in web mercator coordinates
p = figure(x_range=(-8184831.46,-8190000.00 ), y_range=(5701314.14, 5710000.00),
           x_axis_type="mercator", y_axis_type="mercator")
p.add_tile(tile_provider)

curdoc().add_root(p)