%%%%%%%%%%%%%%%%%%% METODI DEL CALCOLO SCIENTIFICO: PROJECT %%%%%%%%%%%%%%%%%%%%
% Team members:
% Mattia Pennati - 793375
% Andrea Spreafico - 793317
% Francesco Prete - 793389
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% IMPORT MATRIX %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%matrix file 'matrixname.mat' structure:
% file[Problem[name, title, A, id, date, author, ed, kind, notes]]
%A = the real matrix
%Access to a specific field (eg. title): file.Problem.title / ...

%import 'MatriciSparse/******.mat, ***** = matrix name
matrix = load('Matrici Non Definite Positive/PR02R.mat');
%size --> (1: nrow, 2: ncol), square matrix: nrow = ncol --> size(A,1)=size(A,2)
size = size(matrix.Problem.A,1);

%display matrix name:
name = strsplit(matrix.Problem.name, "/");
disp("Matrix name: "+name{1});

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% SOLVE MATRIXES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Use the 'mldivided' package to solve the input matrixes and, for each
% matrix, store:
% - solution
% - relative error
% - execution infos (time and memory usage)

%OBS: for each matrix suppose b = A*xe where xe = [1; 1; 1; ....]
%parameters of the linear system associated to the matrix is:
A = matrix.Problem.A;
xe = ones(size,1);
b = A * xe;
    
%profiler: check memory allocated, execution time and other useful information
profile -memory on
%use mldivide to solve the linear system

%%%Sparse linear systems solver: mldivide(A,b) = A\b

spparms('spumoni',1); %use it if you wanna trace the mldivide decisions to 
% solve the linear system (see the tests used to choose the best linear
% solver and)
x = A\b; %x = mldivide(A,b); %unused alternative way to A\b

%%% Ax = b --> x = solution

%save profiler stats (time, memory, ....)
stats = profile('info');
%close profiler
profile -memory off
profile clear

%store results: 
%result
matrix.Problem.solution = x; 
%relative error
matrix.Problem.relative_error = (norm(x-xe)/norm(xe));
%execution time [seconds]
matrix.Problem.execution_time = stats.FunctionTable.TotalTime; 
%allocated memory [byte/1024/1024 --> Mb]
matrix.Problem.allocated_mem = stats.FunctionTable.TotalMemAllocated;
matrix.Problem.allocated_mem = matrix.Problem.allocated_mem/1024/1024;

%Print results:
disp("Execution time: "+matrix.Problem.execution_time+" s");
disp("Allocated memory: "+matrix.Problem.allocated_mem+" Mb");
disp("Relative error: "+matrix.Problem.relative_error);

%clear workspace
clear

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%