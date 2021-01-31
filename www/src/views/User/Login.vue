<template>
  <v-card class="mx-auto mt-5 py-5" max-width="480">
    <v-form ref="form">
      <v-row class="ma-4">
        <v-text-field v-model="phoneNumber" label="请输入手机号"> </v-text-field>
        <v-btn @click="validatePhone" class="ma-4"> 获取验证码 {{ is }} </v-btn>
      </v-row>
      <v-row class="ma-4" v-show="isPhoneOk">
        <v-text-field v-model="veriCode" label="请输入验证码"> </v-text-field>
        <v-btn @click="validateVeriCode" class="ma-4"> 注册并登陆 </v-btn>
      </v-row>
      <v-btn color="red lighten-1" v-show="showErrorInfo" v-text="errorInfo"></v-btn>
    </v-form>
  </v-card>
</template>

<script>
export default {
  data: () => ({
    phoneNumber: "",
    isPhoneOk: false,
    showErrorInfo: false,
    errorInfo: "",
    veriCode: "",
    isVeriCodeOk: "",
  }),
  watch: {
    validPhone() {},
  },
  methods: {
    validatePhone() {
      const regex = /^1[34578]\d{9}$/;

      if (regex.test(this.phoneNumber)) {
        this.isPhoneOk = true;
        this.showErrorInfo = false;
      } else {
        this.showErrorInfo = true;
        this.errorInfo = "请输入正确的手机号";
        this.phoneNumber = "";
      }
    },
    validateVeriCode() {
      if (this.veriCode.length === 6) {
        this.isVeriCodeOk = true;
        this.showErrorInfo = false;
      } else {
        this.showErrorInfo = true;
        this.errorInfo = "请输入正确的验证码";
        this.veriCode = "";
      }
    },
  },
};
</script>
