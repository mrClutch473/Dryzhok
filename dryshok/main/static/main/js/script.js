 // ========== ФУНКЦИИ ДЛЯ МЕНЮ ==========
function scrollToSection(sectionId) {
    const element = document.getElementById(sectionId);
        if (element) {
            element.scrollIntoView({ behavior: 'smooth' });
        } else {
            console.warn('Элемент с id ' + sectionId + ' не найден');
            }
        }

// Мобильное меню
const menuToggle = document.querySelector('.menu-toggle');
const menuButtons = document.querySelector('.menu-buttons');

if (menuToggle && menuButtons) {
    menuToggle.addEventListener('click', () => {
        menuButtons.classList.toggle('active');
            });
        }

// ========== ГАЛЕРЕЯ С ЛИСТАНИЕМ ==========
// Используем DOMContentLoaded, чтобы убедиться, что все элементы загружены
document.addEventListener('DOMContentLoaded', function() {
console.log('Страница загружена, инициализация галереи...');

const slides = document.querySelectorAll('.slide');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');

console.log('Найдено слайдов:', slides.length);
console.log('Кнопка Prev:', prevBtn);
console.log('Кнопка Next:', nextBtn);

if (slides.length === 0) {
    console.error('Слайды не найдены! Проверьте класс .slide');
    return;
}

let currentIndex = 0;
const totalSlides = slides.length;

// Функция обновления активного слайда
function updateSlides(index) {
    slides.forEach((slide, i) => {
    if (i === index) {
        slide.classList.add('active');
    } else {
        slide.classList.remove('active');
                    }
                });
                console.log('Текущий слайд:', index + 1); }

// Следующий слайд
function nextSlide() {
    currentIndex = (currentIndex + 1) % totalSlides;
    updateSlides(currentIndex); }

// Предыдущий слайд
function prevSlide() {
currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
updateSlides(currentIndex);}

// Добавляем обработчики для кнопок
if (prevBtn && nextBtn) {
    prevBtn.addEventListener('click', function(e) {
    e.preventDefault();
    prevSlide();
});
    nextBtn.addEventListener('click', function(e) {
    e.preventDefault();
    nextSlide();
});
    console.log('Кнопки галереи активированы');
} else {
    console.error('Кнопки навигации не найдены!');
}

// Добавляем клавиатурную навигацию
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') {
        prevSlide();
    } else if (e.key === 'ArrowRight') {
        nextSlide();
}
});

// Автоматическое переключение слайдов
let autoplayInterval;
let isHovering = false;

const galleryWrapper = document.querySelector('.gallery-wrapper');

if (galleryWrapper) {
    galleryWrapper.addEventListener('mouseenter', () => {
    isHovering = true;
    if (autoplayInterval) {
        clearInterval(autoplayInterval);
}
});
galleryWrapper.addEventListener('mouseleave', () => {
isHovering = false;
startAutoplay();});
}

function startAutoplay() {
    if (autoplayInterval) {
        clearInterval(autoplayInterval);
    }
    autoplayInterval = setInterval(() => {
    if (!isHovering) {
        nextSlide();
}
}, 5000);
}

// Запускаем автопрокрутку
startAutoplay();
console.log('Галерея успешно инициализирована!');
});

// Функция прокрутки к контактам
function scrollToContact() {
    const contactSection = document.getElementById('contact');
            if (contactSection) {
                contactSection.scrollIntoView({ behavior: 'smooth' });
            } else {
                window.scrollTo({
                top: document.body.scrollHeight,
                behavior: 'smooth'
});
}
}

// Получаем элементы
const modal = document.getElementById('volunteerModal');
const volunteerBtn = document.querySelector('.help-cta-btn.secondary');
const closeBtn = document.querySelector('.modal-volunteer-close');
const volunteerForm = document.getElementById('volunteerForm');
const formMessage = document.getElementById('formMessage');

// Проверка: существует ли модальное окно
if (!modal) {
    console.error('Модальное окно с id "volunteerModal" не найдено!');
}

// Открытие модального окна
if (volunteerBtn && modal) {
    volunteerBtn.addEventListener('click', (e) => {
        e.preventDefault();
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
        console.log('Модальное окно открыто'); // Отладка
    });
} else {
    console.error('Кнопка или модальное окно не найдены!');
    console.log('Кнопка:', volunteerBtn);
    console.log('Модальное окно:', modal);
}

// Закрытие модального окна
if (closeBtn && modal) {
    closeBtn.addEventListener('click', () => {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
        // Очищаем сообщение об ошибке при закрытии
        if (formMessage) {
            formMessage.style.display = 'none';
            formMessage.className = 'form-message';
        }
    });
}

// Закрытие при клике вне модального окна
window.addEventListener('click', (e) => {
    if (modal && e.target === modal) {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
});

// Отправка формы
if (volunteerForm && modal) {
    volunteerForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Проверяем, существует ли кнопка отправки
        const submitBtn = document.querySelector('.btn-submit');
        if (!submitBtn) {
            console.error('Кнопка отправки .btn-submit не найдена!');
            return;
        }

        const originalText = submitBtn.textContent;
        submitBtn.textContent = 'Отправка...';
        submitBtn.disabled = true;

        // Очищаем предыдущие сообщения
        if (formMessage) {
            formMessage.style.display = 'none';
            formMessage.className = 'form-message';
        }

        // Собираем данные формы
        const formData = new FormData(volunteerForm);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        try {
            // Отправляем данные на сервер
            const response = await fetch('/submit-volunteer/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (result.success) {
                // Успешная отправка
                if (formMessage) {
                    formMessage.textContent = result.message;
                    formMessage.className = 'form-message success';
                    formMessage.style.display = 'block';
                }
                volunteerForm.reset();

                // Убираем подсветку ошибок
                document.querySelectorAll('.error').forEach(input => {
                    input.classList.remove('error');
                });

                // Закрыть модальное окно через 3 секунды
                setTimeout(() => {
                    if (modal) modal.style.display = 'none';
                    document.body.style.overflow = 'auto';
                    if (formMessage) {
                        formMessage.style.display = 'none';
                        formMessage.className = 'form-message';
                    }
                }, 3000);
            } else {
                // Ошибка валидации
                if (formMessage) {
                    formMessage.textContent = result.message || 'Пожалуйста, исправьте ошибки в форме.';
                    formMessage.className = 'form-message error';
                    formMessage.style.display = 'block';
                }

                // Подсветка полей с ошибками
                if (result.errors) {
                    Object.keys(result.errors).forEach(field => {
                        const input = document.querySelector(`[name="${field}"]`);
                        if (input) {
                            input.classList.add('error');
                        }
                    });
                }
            }
        } catch (error) {
            console.error('Ошибка:', error);
            if (formMessage) {
                formMessage.textContent = 'Произошла ошибка. Пожалуйста, попробуйте позже.';
                formMessage.className = 'form-message error';
                formMessage.style.display = 'block';
            }
        } finally {
            // Возвращаем кнопку в исходное состояние
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
        }
    });
}

// Функция для получения CSRF токена
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Убираем подсветку ошибок при вводе
document.querySelectorAll('.form-control').forEach(input => {
    input.addEventListener('input', () => {
        input.classList.remove('error');
    });
});

document.addEventListener('DOMContentLoaded', function () {

    const donationBtn = document.getElementById('donationBtn');
    const donationModal = document.getElementById('donationModal');
    const donationClose = document.querySelector('.modal-donation-close');
    const copyBtn = document.getElementById('copyBtn');

    console.log('DonationBtn:', donationBtn);
    console.log('Modal:', donationModal);

    // открыть
    if (donationBtn && donationModal) {
        donationBtn.addEventListener('click', () => {
            donationModal.style.display = 'flex';
            document.body.style.overflow = 'hidden';
        });
    } else {
        console.error('Кнопка или модалка не найдены');
    }

    // закрыть
    if (donationClose) {
        donationClose.addEventListener('click', () => {
            donationModal.style.display = 'none';
            document.body.style.overflow = 'auto';
        });
    }

    // клик вне окна
    window.addEventListener('click', (e) => {
        if (e.target === donationModal) {
            donationModal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });

    // копирование
    if (copyBtn) {
        copyBtn.addEventListener('click', () => {
            navigator.clipboard.writeText('4817 7601 6400 4594');
            copyBtn.textContent = 'Скопировано!';
            setTimeout(() => {
                copyBtn.textContent = 'Скопировать номер карты';
            }, 2000);
        });
    }

});