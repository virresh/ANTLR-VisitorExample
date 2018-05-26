if [[ ${1} == '' ]]; then
	#statements
	echo "No grammar name provided ?"
	exit 0
fi

set -e

antlr4='java -jar /usr/local/lib/antlr-4.7.1-complete.jar'
$antlr4 -Dlanguage=Python3 grammar/${1} -visitor -Xexact-output-dir -o .
rm *.tokens *.interp
python pyAntVisitor.py test.py