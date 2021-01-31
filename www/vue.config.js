module.exports = {
  transpileDependencies: ["vuetify"],
  devServer: { // see https://blog.csdn.net/wh_xmy/article/details/87705840
    proxy: {
      "/api/": {
        changeOrigin: true,
        ws: true,
        target: "http://116.62.161.61:80/",
        pathRewrite:{
          '^/api': ''
        }

      },
    },
  },
};
