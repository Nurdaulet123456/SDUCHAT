
    let modal = document.querySelector('.modal');
    let close__btn = document.querySelector('.close__btn');
    let user_btn = document.querySelector('.user_btn');
    let set_btn = document.querySelector('.set_btn');
    let message_right = document.querySelectorAll('.message-send-right');
    let on = document.querySelector('.on')
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
