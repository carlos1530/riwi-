// let variable1 =1;
// let variable2 =6;
// let suma = variable1+variable2;
// console.log(suma); 

// let resta = variable1-variable2;
// console.log("Esta es la resta: " , resta);

// let multiplicacion = variable1*variable2;
// console.log(multiplicacion);

// let division = variable1/variable2;
// console.log(division);

function suma(){
    let variable1 = document.getElementById("variable1").value;
    let variable2 = document.getElementById("variable2").value;
    num1 = parseInt(variable1);
    num2 = parseInt(variable2);
    
    let suma = num1 + num2;
    let resta = num1 - num2;
    let multiplicacion = num1 * num2;
    let division = num1 / num2;  
    
    document.getElementById("resultado").innerText = "suma: "+ suma + "\nResta: " + resta + "\nmultiplicacion: " + multiplicacion + "\ndivision: " + division; 

}