# localsearch-for-TSP

This program reads a point data file and outputs an approximate solution to the TSP (traveling salesman problem) using multiple search algorithms.

First, the approximate solution is obtained using the Nearest Neighbor method, which is a kind of local search method, and then the approximate solution is updated using the ILS(iterated local) with double blidge and 2-opt edge recombination.

If we get a better approximation, we run ILS on that solution again with double blidge and 2-opt.

After doing the above for a predetermined number of times (loop_num), we output the evaluation values of the approximate solution and the graph.

## Getting Started

Please specify the point data file as the command line argument and execute it.

ex. python local_s.py < a280.dat

The point data should be in the format of the sample data, a280.dat.


## Dependencies

* matplotlib3.4.3

---

# localsearch-for-TSP

点データファイルを読み込み、複数の探索アルゴリズムを用いてTSP (traveling salesman problem)の近似解を出力します。

まず局所探索法の一種であるNearest Neighbor法を用いて近似解を求め、その後、double blidgeで辺の組み換え2-optによる反復局所探索法 (Iterated Local Search) で近似解の更新を試みます。
より良い近似解が得られた場合、その解へ再びdouble blidgeと2-optでILSをおこないます。

既定の回数（loop_num）だけ上記の処理をおこなった後、近似解の評価値とグラフを出力します。

## 実行方法

コマンドライン引数で点データファイルを指定し実行してください。

例：python local_s.py < a280.dat

点データはサンプルデータであるa280.datの形式に合わせてください。

## 依存ライブラリ

* matplotlib3.4.3
