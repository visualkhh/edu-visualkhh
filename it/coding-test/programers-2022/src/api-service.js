
class ApiService {

    /* return
        [
          "Java",
          "JavaFX Script",
          "JavaScript",
          "Join Java"
        ]
     */
    getKeyword(keyword) {
        return this.getJson(`https://wr4a6p937i.execute-api.ap-northeast-2.amazonaws.com/dev/languages?keyword=${keyword}`);
    }

    getJson(url) {
        return fetch(url)
            .then(response => response.json())
            .then(json => json);
    }
}



export default new ApiService();