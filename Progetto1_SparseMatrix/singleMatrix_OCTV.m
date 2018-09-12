%%%%%%%%%%%%%%%%%%% METODI DEL CALCOLO SCIENTIFICO: PROJECT %%%%%%%%%%%%%%%%%%%%
%Team members:
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
warning("off")
matrix = load('Matrici Non Definite Positive/ex19.mat');
%size --> (1: nrow, 2: ncol), square matrix: nrow = ncol --> size(A,1)=size(A,2)
size = size(matrix.Problem.A,1);

%display matrix name:
name = strsplit(matrix.Problem.name, "/");
printf("Matrix name: %s ", name{1,2});

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
profile on
%use mldivide to solve the linear system

%%%Sparse linear systems solver: mldivide(A,b) = A\b

spparms("spumoni") %use it if you wanna trace the mldivide decisions to 
% solve the linear system (see the tests used to choose the best linear
% solver and)
x = A\b; %x = mldivide(A,b); %unused alternative way to A\b

%%% Ax = b --> x = solution

%save profiler stats (execution time, ....)
stats = profile('info');
%close profiler
profile off
profile clear

%store results: 
%result
matrix.Problem.solution = x; 
%relative error
matrix.Problem.relative_error = (norm(x-xe)/norm(xe));
%execution time [seconds]
matrix.Problem.execution_time = stats.FunctionTable.TotalTime;  

%Print results:
printf("\nExecution time: %d s\n", matrix.Problem.execution_time);
printf("Relative error: %d \n ", matrix.Problem.relative_error);

%clear workspace
clear

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
