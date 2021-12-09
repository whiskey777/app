console.log('HELLO')

let metalsUrl = 'http://localhost:8000/api/metals/'
let getMetals = () => {
    fetch(metalsUrl)
    .then(response =>response.json())
    .then(data => {
        console.log(data)
        buildMetals(data)
    })
}

let buildMetals = (metals) => {
    let metalsWrapper = document.getElementById('metals-wrapper')
    for (let i = 0; metals.length > i; i++){
        let metal = metals[i]
        
        let metalCard = `
                <div class = >
                    <p>${metal.name}</p>
                </div>    
        `
        metalsWrapper.innerHTML += metalCard
    }
}

getMetals()
