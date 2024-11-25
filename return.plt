set terminal pngcairo size 880,440 enhanced font 'Verdana,18' linewidth 1
set output "return.png"

set key bottom right
set xlabel "t"
set ylabel "r_{φ^{4}}(t)"
set xtics format '%.t×10^{%T}' add ("0" 0)
set border lw 2

plot "returns.dat" u 1 w lines ls 2 lw 0.8 dt 1  notitle, \



