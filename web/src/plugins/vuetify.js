import Vue from "vue";
import Vuetify from "vuetify/lib/framework";

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    options: {
      customProperties: true,
    },
    themes: {
      light: {
        FountainBlue: "#59A9A9",
        White: "#FFFFFF",
        DarkRed: "#C21414",
        ChelseaCucumber: "#B5B35D",
        WhiteIce: "#F1F9F5",
        PattensBlue: "#E9F4F6",
        Genoa: "#358379",
        HummingBird: "#D6F0EA",
        Black: "#000000",
        Ciinder: "#212529",
        DimGray: "#696969",
        DarkGray: "#9D9D9D",
        LightGray: "#D3D3D3",
        WhiteSmoke: "#F4F4F4"
      },
    },
  },
});
