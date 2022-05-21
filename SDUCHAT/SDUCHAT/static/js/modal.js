let modal = document.querySelector('.modal');
let close__btn = document.querySelector('.close__btn');
let user_btn = document.querySelector('.user_btn');
let set_btn = document.querySelector('.set_btn');
let message_right = document.querySelectorAll('.message-send-right');
let on = document.querySelector('.on')
const username = JSON.parse(document.getElementById('json-name').textContent);
const email = JSON.parse(document.getElementById('json-email').textContent);
let userModal = document.querySelector('.modal__user')
let userName = document.querySelectorAll('#Name')

set_btn.addEventListener('click', (e) => {
    e.preventDefault();
    console.log('click')
    modal.classList.toggle('show')
})

close__btn.addEventListener('click', (e) => {
    e.preventDefault()
    modal.classList.toggle('show');
})


// Rigth Mouse

for (let i = 0; i < message_right.length; i++) {

    message_right[i].addEventListener('contextmenu', (e) => {
        e.preventDefault();

        on.classList.toggle('block')

    })

}

// User_Modal

for (let i = 0; i < userName.length; i++) {
    userName[i].addEventListener('click', (e) => {
        e.preventDefault()
        userModal.classList.toggle('show')
    })
}

user_btn.addEventListener('click', (e) => {
    e.preventDefault()
    userModal.classList.toggle('show');
})