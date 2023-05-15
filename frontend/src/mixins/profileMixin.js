export const profileMixin = {
    methods: {
        formatDate(date) {
            const monthNames = [
                "Январь", "Февраль", "Март", "Апрель",
                "Май", "Июнь", "Июль", "Август",
                "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
            ]
            let arr = date.split('-');
            return arr[2] + ' ' + monthNames[+arr[1] - 1]+ `'${arr[0].slice(2)}`
        },
        fullName(name, surname, patronymic) {
            return surname + ' ' + name +
                (patronymic.length > 0 ? ' ' + patronymic : '')
        }
    }
};