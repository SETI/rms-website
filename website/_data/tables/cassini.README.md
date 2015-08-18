use only columns listed below
if you want to add a column not shown below, 
you must also add it the html in the cassini_tables.html template
 
	- column_labels: 
	     - Volume ID
	     - Bundled Volumes
	     - Browse Images
	     - Calibrated Images
	     - Footprint Link
	     - Index File
	     - Spacecraft Clock (SCLK) range  
	     - Data Set
	     - Volume ID List

in the markdown file, call the template like so:

		{% assign table_name = "Cassini UVIS Releases" %}
		{% assign table_desc = "A listing of Cassini UVIS Releases" %}
		{% assign table_data = site.data.tables['cassini_uvis_access'] %}
		{% include data_table.html %}
