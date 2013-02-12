google-maps-wms
===============

WMS service for downloading map tiles from [Google Maps](http://maps.google.com). It cannot display tiles in zoom other than standard [tile zoom levels](https://developers.google.com/maps/documentation/staticmaps/#Zoomlevels). If you try to get image in such a non-standard zoom level then you get image with nearest standard zoom level. But this is not a big limit if you use this service in (JOSM)[http://josm.openstreetmap.de/] together with [zoom plugin](https://github.com/gumik/josm-zoom).

Usage
-----

Just run it with `python google_maps_wms.py`. Service will listen on port 8000. You can optionally set your Google Developers API Key in `googleApiKey` variable inside the source code.

Note
----
Remember that you cannot use Google Maps to create your own maps.
"You must not copy, translate, modify, or create a derivative work (including creating or contributing to a database) of, or publicly display any Content or any part thereof except as explicitly permitted under these Terms."\[1\]
\[1\][https://developers.google.com/maps/terms](https://developers.google.com/maps/terms)
