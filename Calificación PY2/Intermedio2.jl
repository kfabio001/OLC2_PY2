#array = [32, 21, 7, 89, 56, 909, 109, 2];
array=56;
println("=======================================================================");
println("==================================IF===================================");
println("=======================================================================");

if (array > 50) 
    println("IF CORRECTO");
elseif (array == 56) 
    println("IF INCORRECTO");
else
    println("IF INCORRECTO");
end;

println("");
println("=======================================================================");
println("=============================IFs ANIDADOS==============================");
println("=======================================================================");
aux = 10;
if aux > 0
    println("PRIMER IF CORRECTO");
    if true && (aux == 1)
        println("SEGUNDO IF INCORRECTO");
    elseif aux > 10
        println("SEGUNDO IF INCORRECTO");
    else
        println("SEGUNDO IF CORRECTO");
    end;
elseif aux <= 3
    println("PRIMER IF INCORRECTO");
    if true && (aux == 1)
        println("SEGUNDO IF INCORRECTO");
    elseif aux > 10
        println("SEGUNDO IF INCORRECTO");
    else
        println("SEGUNDO IF CORRECTO");
    end;
elseif aux == array
    println("PRIMER IF INCORRECTO");
    if true && (aux == 1)
        println("SEGUNDO IF INCORRECTO");
    elseif aux > 10
        println("SEGUNDO IF INCORRECTO");
    else
        println("SEGUNDO IF CORRECTO");
    end;
end;

println("");
println("=======================================================================");
println("=================================WHILE=================================");
println("=======================================================================");

index = 0::Int64;

while (index >= 0) 

    if (index == 0) 
         index = index + 100;
    elseif (index > 50) 
         index = index / 2 - 25;
    else 
         index = (index / 2) - 1;
    end;

    println(index);
end;

println("");
println("=======================================================================");
println("================================WHILE-2================================");
println("=======================================================================");

index = -2;
index = index + 1;

while (index != 12)
     index = index + 1;
    if (index == 0 || index == 1 || index == 11 || index == 12) 
        println("*********************************************************************************************************");
    elseif (index == 2) 
        println("**********  ***************  ******                 ******                 ******              **********");
    elseif (index >= 3 && index <= 5) 
        println("**********  ***************  ******  *********************  *************  ******  **********************");
    elseif (index == 6) 
        println("**********  ***************  ******                 ******                 ******  **********************");
    elseif (index >= 7 && index <= 9) 
        println("**********  ***************  ********************   ******  *************  ******  **********************");
    elseif (index == 10) 
        println("**********                   ******                 ******  *************  ******              **********");
    end;
end;

println("");
println("=======================================================================");
println("=============================TRANSFERENCIA=============================");
println("=======================================================================");

a = -1;
while (a < 5)
     a = a + 1;
    if a == 3
        print("a");
        continue;
    elseif a == 4
        println("b");
        break;
    end;

    print("El valor de a es: ", a, ", ");
end;

println("Se debió imprimir");

println("");
println("=======================================================================");
println("==================================FOR==================================");
println("=======================================================================");

for i in 0:9

    output = "";
    for j in 0:(10 - i)
        output = output * " ";
    end;

    for k in 0:i 
        output = output * "* ";
    end;
    println(output);

end;

println("");
println("=======================================================================");
println("=================================FOR-2=================================");
println("=======================================================================");

#arr = [1,2,3,4,5,6];
for i in 1:6
    println(i == 1, i == 2, i== 3, i == 4, i == 5, i == 6);
end;

println("");
println("=======================================================================");
println("=================================FOR-3=================================");
println("=======================================================================");
for e in 1:6
    if(6 > e)
        println(e*e,e*e,e*e,e*e,e*e,e*e);
    end;
end;
println("");
println("=======================================================================");
println("=================================FOR-4=================================");
println("=======================================================================");
#for letra in "Calificacion de Intermedio"
 #   println(letra);
#end;
