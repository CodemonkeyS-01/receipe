console.log("connected")

function Topro(){
    document.addEventListener('DOMContentLoaded', function(){
        document.querySelectorAll('button').forEach(function(button){
            button.onclick = function(){
            displayControl(`ingredient_${this.dataset.id}`, `procedure_${this.dataset.id}`, this.id)
            
                
        }})})
    }

function displayControl(close_id, on_id, btn_id){
    const ingred = document.querySelector(`#${close_id}`)
    const proced = document.querySelector(`#${on_id}`)
    const btn = document.querySelector(`#${btn_id}`)
    if(ingred.style.display === "none"){
        ingred.style.display = "block"
        proced.style.display = "none"
        btn.innerHTML = "To procedure"
    } else{
        ingred.style.display ="none"
        proced.style.display = "block"
        btn.innerHTML = "To ingredients"
    }
}
    



Topro()