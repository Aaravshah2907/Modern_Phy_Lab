gnuplot -p experiment7_graph.gp < experimental_readings.csv
qlmanage -t -s 1000 -o . Experimental_graph.svg
cp Experimental_graph.svg.png Experimental_graph.png
rm Experimental_graph.svg.png