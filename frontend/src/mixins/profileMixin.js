export const profileMixin = {
    methods: {
        formatDate(date, flag = true) {
            const monthNames = [
                "Января", "Февраля", "Марта", "Апреля",
                "Мая", "Июня", "Июля", "Августа",
                "Сентября", "Октября", "Ноября", "Декабря"
            ]
            let arr = date.split('-');

            let year = flag ? '\'' + arr[0].slice(2) : ' ' +
                arr[0];

            let month = monthNames[+arr[1] - 1];

            let day = arr[2].slice(0, 1) === '0' ? arr[2].slice(-1) :
                arr[2]

            return day + ' ' + month + year
        },
        fullName(name, surname, patronymic) {
            return surname + ' ' + name +
                (patronymic.length > 0 ? ' ' + patronymic : '')
        }
    }
};