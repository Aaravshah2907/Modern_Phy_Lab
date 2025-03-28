python3 calculations.py
gnuplot -p experiment11_graph.gp < numbers.csv
qlmanage -t -s 1000 -o . Experimental_graph.svg
cp Experimental_graph.svg.png Experimental_graph.png
rm Experimental_graph.svg.png
rm Experimental_graph.svg