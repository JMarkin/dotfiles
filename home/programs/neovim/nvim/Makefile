tests-data: tests/data/bigdata.json tests/data/bigdata.yml

tests/data/bigdata.json:
	+mkdir -p tests/data
	+curl -L --progress-bar -o $@ \
		"https://raw.githubusercontent.com/miloyip/nativejson-benchmark/master/data/canada.json"

tests/data/bigdata.yml:
	+mkdir -p tests/data
	+base64 /dev/urandom | head --bytes $$(( 5*1024*1024 )) > $@
