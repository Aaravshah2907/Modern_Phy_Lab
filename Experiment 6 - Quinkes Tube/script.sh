gnuplot -p experiment6_graph.gp < experimental_data.csv
qlmanage -t -s 1000 -o . Experimental_graph_3.svg
cp Experimental_graph_3.svg.png Experimental_graph_3.png
rm Experimental_graph_3.svg.png
rm Experimental_graph_3.svg