
const converter = document.querySelector('#converter')

converter.addEventListener('click', ()=>{
    event.preventDefault()
    const medida1 = document.getElementById('medida1').value
    const medida2 = document.getElementById('medida2').value
    document.getElementById('resultado').value = ''
    let num1 = document.getElementById('num1').value
    let num2

    switch(medida2){

        case 'jardas':
            switch(medida1){
                case 'jardas':
                    num2 = num1 * 1
                    break
                case 'pes':
                    num2 = num1 * 3
                    break
                case 'polegadas':
                    num2 = num1 * 36
                    break
                case 'milhas':
                    num2 = num1/1760
                    break
            }
        break

        case 'pes':
            switch(medida1){
                case 'jardas':
                    num2 = num1/3
                    break
                case 'pes':
                    num2 = num1 * 1
                    break
                case 'polegadas':
                    num2 = num1 * 12
                    break
                case 'milhas':
                    num2 = num1/5280
                    break
            }
        break

        case 'polegadas':
            switch(medida1){
                case 'jardas':
                    num2 = num1/36
                    break
                case 'pes':
                    num2 = num1/12
                    break
                case 'polegadas':
                    num2 = num1 * 1
                    break
                case 'milhas':
                    num2 = num1/63360
                    break
                    
            }
        break
        
        case 'milhas':
            switch(medida1){
                case 'jardas':
                    num2 = num1 * 1760
                    break
                case 'pes':
                    num2 = num1 * 5280
                    break
                case 'polegadas':
                    num2 = num1 * 63360
                    break
                case 'milhas':
                    num2 = num1 * 1
                    break
            }
        break
    }

    document.getElementById('resultado').value = num2
})