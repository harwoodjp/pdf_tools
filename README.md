Wrapping Ghostscript + other things for scriptable PDF convenience 

Done

* `pdf_tools verify in.pdf`
* `pdf_tools split in.pdf out_dir png|pdf`

Todo

* `pdf_tools compress in.pdf out.pdf`
* `pdf_tools join in1.pdf in2.pdf in3.pdf out.pdf`

Run

* `docker-compose up pdf_tools -d`
* `docker exec -it pdf_tools bash`
* e.g. `python pdf_tools/app.py verify in.pdf`

Debug

* Make sure Ghostscript is installed
* `-v` flag for verbose logging
