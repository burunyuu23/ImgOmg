export const imageMixin = {
    data() {
      return {
          names: ['b', 'Kb', 'Mb'],
          names_index: 0
      }
    },
    methods: {
        getBase64FileSize(base64String) {
            // Удалите информацию о типе файла из base64-строки
            const base64WithoutType = base64String.replace(/^data:image\/[a-z]+;base64,/, '');

            // Декодируйте base64 в бинарные данные
            const binaryData = atob(base64WithoutType);

            // Получите размер данных
            let fileSize = binaryData.length;

            fileSize = this.anotherFormat(fileSize)

            // Верните размер данных
            return fileSize.toFixed(2);
        },
        anotherFormat(fileSize) {
            this.names_index = 0
            while (fileSize > 1024) {
                fileSize /= 1024;
                this.names_index++;
            }
            return fileSize;
        },
        getFileSize(fileSize) {
            return `${this.anotherFormat(fileSize).toFixed(2)} ${this.names[this.names_index]}`
        },
        getFileSizeFromBase64(base64String) {
            return `${this.getBase64FileSize(base64String)} ${this.names[this.names_index]}`
        }
    }
};