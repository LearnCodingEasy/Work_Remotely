<template>
  <div class="wrapper_page_login">
    <div class="inner_page_login">
      <div class="container mx-auto">
        <div class="wrapper_content_page_login flex justify-center items-center">
          <div class="inner_content_page_login">
            <!-- Signup -->
            <div class="mobile_body_dark">
              <span class="voice_up"> </span>
              <span class="voice_down"> </span>
              <span class="power"> </span>
              <span class="sonser"> </span>
              <span class="voice"> </span>
              <span class="carme"> </span>
              <div class="mobile_content">
                <form class="">
                  <prime_card class="prime_card_form_signup">
                    <template #header>
                      <div class="flex justify-between items-center w-full">
                        <div class="text font-bold text-5xl">Signup</div>
                        <div class="image_logo">
                          <img src="../../assets/Images/Messenger_80x80.png" class="" alt="" />
                        </div>
                      </div>
                    </template>
                    <template #content>
                      <prime_fluid class="prime_card_form_signup_content">
                        <div class="">
                          <div class="flex">
                            <!-- First name -->
                            <div class="mr-1">
                              <prime_input_text
                                placeholder="First name"
                                v-model="formSignup.name"
                              />
                            </div>
                            <!-- Surname -->
                            <div class="ml-1">
                              <prime_input_text
                                placeholder="Surname"
                                v-model="formSignup.surname"
                              />
                            </div>
                          </div>
                          <!-- Mobile number or email address -->
                          <div class="col-span-full">
                            <prime_input_text
                              placeholder="Mobile number or email address"
                              v-model="formSignup.email"
                            />
                          </div>
                          <!-- password1 -->
                          <div class="col-span-full">
                            <prime_input_password
                              placeholder="New Password"
                              v-model="formSignup.password1"
                            />
                          </div>
                          <!-- password2 -->
                          <div class="col-span-full">
                            <prime_input_password
                              placeholder="Repeat password"
                              v-model="formSignup.password2"
                            />
                          </div>
                          <!-- Date of birth -->
                          <div class="col-span-full">Date of birth</div>
                          <div class="col-span-full">
                            <div class="flex flex-col md:flex-row gap-2">
                              <!-- Day -->
                              <prime_input_group>
                                <prime_date_picker v-model="day" view="day" dateFormat="dd" />
                              </prime_input_group>
                              <!-- Month -->
                              <prime_input_group>
                                <prime_date_picker v-model="month" view="month" dateFormat="mm" />
                              </prime_input_group>
                              <!-- Year -->
                              <prime_input_group>
                                <prime_date_picker v-model="year" view="year" dateFormat="yy" />
                              </prime_input_group>
                            </div>
                          </div>
                          <!-- Gender -->
                          <div class="col-span-full">Gender</div>
                          <div class="flex flex-col md:flex-row gap-2">
                            <prime_input_group>
                              <prime_radio_button
                                v-model="formSignup.gender"
                                inputId="ingredient1"
                                name="gender"
                                value="Female"
                              />
                              <label for="ingredient1" class="ml-2"> Female </label>
                            </prime_input_group>
                            <prime_input_group>
                              <prime_radio_button
                                v-model="formSignup.gender"
                                inputId="ingredient2"
                                name="gender"
                                value="Male"
                              />
                              <label for="ingredient2" class="ml-2"> Male </label>
                            </prime_input_group>

                            <prime_input_group>
                              <prime_radio_button
                                v-model="formSignup.gender"
                                inputId="ingredient3"
                                name="gender"
                                value="Custom"
                              />
                              <label for="ingredient3" class="ml-2"> Custom </label>
                            </prime_input_group>
                          </div>
                        </div>
                      </prime_fluid>
                    </template>
                    <template #footer>
                      <div class="flex justify-center gap-2">
                        <button
                          type="submit"
                          class="d_block_important mt-1 mx-auto w_50 bg-green-500 py-3 px-5 rounded text-white"
                          @click.prevent="submitFormSignup"
                        >
                          Signup
                        </button>
                      </div>
                    </template>
                    <!-- Errors -->
                    <template v-if="errorsSignup.length > 0">
                      <prime_toast />
                    </template>
                  </prime_card>
                </form>
              </div>
            </div>
            <!-- Log in -->
            <div class="mobile_body_dark">
              <span class="voice_up"> </span>
              <span class="voice_down"> </span>
              <span class="power"> </span>
              <span class="sonser"> </span>
              <span class="voice"> </span>
              <span class="carme"> </span>
              <div class="mobile_content">
                <form class="">
                  <prime_card class="prime_card_form_login">
                    <template #header>
                      <div class="flex justify-between items-center w-full">
                        <div class="text font-bold text-5xl">Log in</div>
                        <div class="image_logo">
                          <img src="../../assets/Images/Messenger_80x80.png" class="" alt="" />
                        </div>
                      </div>
                    </template>
                    <template #content>
                      <prime_fluid class="prime_card_form_signup_content">
                        <div class="input_email">
                          <!-- Mobile number or email address -->
                          <div class="col-span-full">
                            <prime_input_text
                              placeholder="Mobile number or email address"
                              v-model="formLogin.email"
                            />
                          </div>
                        </div>
                      </prime_fluid>
                      <!-- password -->
                      <div class="input_password">
                        <prime_input_password
                          placeholder="Your Password"
                          v-model="formLogin.password"
                        />
                      </div>
                      <div class="Forgotten_password">
                        <a href="#" class="text-blue-600 mx-auto my-2 block text-center"
                          >Forgotten password?</a
                        >
                        <hr />
                      </div>
                    </template>
                    <template #footer>
                      <div class="row">
                        <!-- Errors -->
                        <template v-if="errorsLogin.length > 0">
                          <prime_toast></prime_toast>
                        </template>
                        <!-- Login -->
                        <div class="mt-2">
                          <button
                            type="submit"
                            class="d_block_important mt-1 mb-2 mx-auto w_100 bg-red-500 py-3 px-5 rounded text-white"
                            @click.prevent="submitFormLogin"
                          >
                            Log In
                          </button>

                          <!-- Button Signup -->
                        </div>
                      </div>
                    </template>
                  </prime_card>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <prime_toast />
  </div>
</template>

<script>
import axios from 'axios'
// eslint-disable-next-line no-unused-vars
import { RouterLink } from 'vue-router'
import { useUserStore } from '@/stores/user'
export default {
  name: 'loginView',
  setup() {
    const userStore = useUserStore()
    return {
      userStore,
    }
  },
  data() {
    return {
      formLogin: {
        email: '',
        password: '',
      },
      errorsLogin: [],

      // Signup
      formSignup: {
        name: '',
        surname: '',
        email: '',
        date_of_birth: null,
        gender: '',
        password1: '',
        password2: '',
      },
      day: '',
      month: '',
      year: '',
      errorsSignup: [],
    }
  },
  methods: {
    async submitFormLogin() {
      this.errorsLogin = []
      if (this.formLogin.email === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User Name missing',
          detail: 'Your name is missing',
          life: 3000,
        })
        this.errorsLogin.push('Your e-mail is missing')
      }
      if (this.formLogin.password === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User password is missing',
          detail: 'Your password is missing',
          life: 3000,
        })
        this.errorsLogin.push('Your password is missing')
      }
      if (this.errorsLogin.length === 0) {
        await axios
          .post('/api/login/', this.formLogin)
          .then((response) => {
            this.userStore.setToken(response.data)
            // console.log('response.data: ', response.data)
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access
          })
          .catch((error) => {
            console.log('error', error)
            if (error.response.data.detail) {
              // Code If True
              this.$toast.add({
                severity: 'error',
                summary: 'Error Message',
                detail: `${error.response.data.detail}`,
                life: 6000,
              })
            }

            this.errorsLogin.push(
              'The email or password is incorrect! Or the user is not activated!',
            )
          })
      }
      if (this.errorsLogin.length === 0) {
        await axios
          .get('/api/me/')
          .then((response) => {
            this.userStore.setUserInfo(response.data)
            this.$router.push('/')
          })
          .catch((error) => {
            console.log('error', error)
          })
      }
    },
    submitFormSignup() {
      this.errorsSignup = []

      // استخراج اليوم، الشهر، والسنة من كائنات Date وتنسيقها
      const day = this.day.getDate().toString().padStart(2, '0')
      const month = (this.month.getMonth() + 1).toString().padStart(2, '0')
      const year = this.year.getFullYear()

      const formattedDate = `${year}-${month}-${day}`
      this.formSignup.date_of_birth = formattedDate

      if (this.formSignup.name === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User Name missing',
          detail: 'Your name is missing',
          life: 3000,
        })
        this.errorsSignup.push('Your name is missing')
      }
      if (this.formSignup.surname === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User Surname missing',
          detail: 'Your Surname is missing',
          life: 3000,
        })
        this.errorsSignup.push('Your surname is missing')
      }
      if (this.formSignup.email === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User Is missing',
          detail: 'Your e-mail is missing',
          life: 3000,
        })
        this.errorsSignup.push('Your e-mail is missing')
      }
      if (this.formSignup.password1 === '') {
        this.$toast.add({
          severity: 'error',
          summary: 'User passwordIs missing',
          detail: 'Your password is missing',
          life: 3000,
        })
        this.errorsSignup.push('Your password is missing')
      }
      if (this.formSignup.password1 !== this.formSignup.password2) {
        this.$toast.add({
          severity: 'error',
          summary: 'User  password does not match',
          detail: 'Your password  does not match',
          life: 3000,
        })
        this.errorsSignup.push('The password does not match')
      }
      if (this.errorsSignup.length === 0) {
        axios
          .post('/api/signup/', this.formSignup)
          .then((response) => {
            if (response.data.message === 'success') {
              if (response.data.email_sent) {
                this.$toast.add({
                  severity: 'success',
                  summary: 'User Registered',
                  detail: 'Please activate your account by clicking the link sent to your email.',
                  life: 3000,
                })
              }
              this.$toast.add({
                severity: 'success',
                summary: 'User Is Registered',
                detail: 'Please activate your account by clicking your email link',
                life: 3000,
              })
              this.formSignup.name = ''
              this.formSignup.surname = ''
              this.formSignup.email = ''
              this.formSignup.date_of_birth = ''
              this.formSignup.gender = ''
              this.formSignup.password1 = ''
              this.formSignup.password2 = ''
              // this.$router.push('/loginView')
              window.location.reload()
            } else {
              const data = JSON.parse(response.data.message)
              this.$toast.add({
                severity: 'error',
                summary: 'Error Message',
                detail: 'Message Content Something went wrong. Please try again',
                life: 6000,
              })
              for (const key in data) {
                this.errors.push(data[key][0].message)
              }
              console.log(`Bad`, this.formSignup.date_of_birth)
              console.log(`Day`, this.day)
              console.log(`month`, this.month)
              console.log(`year`, this.year)
            }
          })
          .catch((error) => {
            console.log('error', error)
          })
      }
    },
  },
  mounted() {
    document.title = 'Trello | Login'
  },
}
</script>

<style lang="scss">
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

.wrapper_page_login {
  padding: 0;
  margin: 0;
  height: 99.99vh;
  max-height: 100vh;
  overflow: hidden;
  background-image: linear-gradient(to right, #5b66f6, #e54da4);
  .inner_page_login {
    height: 100%;
    .container {
      height: 100%;
      .wrapper_content_page_login {
        height: 100%;
        .inner_content_page_login {
          position: relative;
          height: 85%;
          width: 100%;
          margin: auto;
          display: grid;
          grid-gap: 5%;
          justify-content: space-between;
          align-items: center;
          // screen and (max-width: 568px)
          // @include MediaQueries(Xxs) {}
          @include MediaQueries(Mobile) {
            // background-color: #ffa704;
          }
          // screen and (min-width: 569px) and (max-width: 767px)
          // @include MediaQueries(Xs) {}
          @include MediaQueries(Tablet) {
            // background-color: #b3f5b3;
          }
          // screen and (min-width: 768px) and (max-width: 991px)
          // @include MediaQueries(Md) {}
          @include MediaQueries(laptop) {
            // background-color: #b3d4f5;
          }
          // screen and (min-width: 992px) and (max-width: 1199px)
          // @include MediaQueries(Lg) {  }
          @include MediaQueries(laptopLg) {
          }
          // screen and (min-width: 1200px) and (max-width: 1399px)
          // @include MediaQueries(Xlg) {}
          @include MediaQueries(Desktop) {
            grid-template-columns: repeat(auto-fill, minmax(35%, 1fr));
          }
          // screen and (min-width: 1400px)
          // @include MediaQueries(Xxlg) {}
          @include MediaQueries(DesktopLg) {
            grid-template-columns: repeat(auto-fill, minmax(35%, 1fr));
          }

          .mobile_body {
            border: 0.5rem solid #130e0e;
            border-radius: 32px;
            -webkit-border-radius: 32px;
            -moz-border-radius: 32px;
            -ms-border-radius: 32px;
            -o-border-radius: 32px;
            height: 100%;
            margin: auto;
            position: relative;
            position: relative;
            // screen and (max-width: 568px)
            // @include MediaQueries(Xxs) {}
            @include MediaQueries(Mobile) {
              &::after {
                content: '📱 568';
                position: absolute;
                top: 0%;
                left: 0px;
                border-radius: 0.5rem;
                z-index: 7;
                font-size: 20px;
                font-weight: bold;
                background-color: #130e0e;
                color: #fff;
                padding: 10px 15px;
              }
            }
            // screen and (min-width: 569px) and (max-width: 767px)
            // @include MediaQueries(Xs) {}
            @include MediaQueries(Tablet) {
              &::after {
                content: '📱 567 767';
                position: absolute;
                top: 0%;
                left: 0px;
                border-radius: 0.5rem;
                z-index: 7;
                font-size: 20px;
                font-weight: bold;
                background-color: #130e0e;
                color: #fff;
                padding: 10px 15px;
              }
            }
            // screen and (min-width: 768px) and (max-width: 991px)
            // @include MediaQueries(Md) {}
            @include MediaQueries(laptop) {
              &::after {
                content: '💻 768 991';
                position: absolute;
                top: 0%;
                left: 0px;
                border-radius: 0.5rem;
                z-index: 7;
                font-size: 20px;
                font-weight: bold;
                background-color: #130e0e;
                color: #fff;
                padding: 10px 15px;
              }
            }
            // screen and (min-width: 992px) and (max-width: 1199px)
            // @include MediaQueries(Lg) {}
            @include MediaQueries(laptopLg) {
              &::after {
                content: '💻➕ 992 1199';
                position: absolute;
                top: 0%;
                left: 0px;
                border-radius: 0.5rem;
                z-index: 7;
                font-size: 20px;
                font-weight: bold;
                background-color: #130e0e;
                color: #fff;
                padding: 10px 15px;
              }
            }
            // screen and (min-width: 1200px) and (max-width: 1399px)
            // @include MediaQueries(Xlg) {}
            @include MediaQueries(Desktop) {
              &::after {
                content: '🖥️ 1200 1399';
                position: absolute;
                top: 0%;
                left: 0px;
                border-radius: 0.5rem;
                z-index: 7;
                font-size: 20px;
                font-weight: bold;
                background-color: #130e0e;
                color: #fff;
                padding: 10px 15px;
                display: none;
              }
              width: 50%;
              overflow-x: hidden;
            }
            // screen and (min-width: 1400px)
            // @include MediaQueries(Xxlg) {}
            @include MediaQueries(DesktopLg) {
              &::after {
                content: '🖥️➕ 1400';
                position: absolute;
                top: 0%;
                left: 0px;
                border-radius: 0.5rem;
                z-index: 7;
                font-size: 20px;
                font-weight: bold;
                background-color: #130e0e;
                color: #fff;
                padding: 10px 15px;
                display: none;
              }
              width: 50%;
            }
            .mobile_content {
              position: relative;
              border-radius: 24px;
              -webkit-border-radius: 24px;
              -moz-border-radius: 24px;
              -ms-border-radius: 24px;
              -o-border-radius: 24px;
              border: 0.2rem solid #130e0e;
              height: 100%;
              background-color: #fff;
              padding: 1rem;
              display: flex;
              justify-content: space-between;
              align-items: center;
              form {
                height: 100%;
                display: flex;
                justify-content: space-between;
                align-items: center;
                width: 100%;
                .prime_card_form_signup {
                  border: none;
                  padding: 0;
                  margin: 0;
                  box-shadow: none;
                  height: 100%;
                  max-height: 100%;
                  overflow: hidden;
                  border-radius: 0px;
                  display: flex;
                  justify-content: center;
                  align-items: center;
                  div.p-card-header {
                    height: 20%;
                    width: 100%;
                    display: flex;
                    align-items: center;
                    width: 100%;
                  }
                  div.p-card-body {
                    padding: 0;
                    margin: 0;
                    margin-bottom: 1rem;
                    height: 80%;
                    display: flex;
                    flex-direction: column;
                    div.p-card-content {
                      height: 80%;
                      .prime_card_form_signup_content {
                        > div {
                          display: flex;
                          flex-direction: column;
                          justify-content: space-between;
                          > div {
                            margin-top: 1rem;
                          }
                        }
                      }
                    }
                    div.p-card-footer {
                      height: 20%;
                      display: flex;
                      justify-content: center;
                      align-items: center;
                    }
                  }
                }
                .prime_card_form_login {
                  border: none;
                  padding: 0;
                  margin: 0;
                  box-shadow: none;
                  height: 100%;
                  max-height: 100%;
                  overflow: hidden;
                  border-radius: 0px;
                  display: flex;
                  justify-content: center;
                  align-items: center;
                  width: 100%;
                  div.p-card-header {
                    height: 20%;
                    width: 100%;
                    display: flex;
                    align-items: center;
                    width: 100%;
                  }
                  div.p-card-body {
                    padding: 0;
                    margin: 0;
                    margin-bottom: 1rem;
                    height: 80%;
                    display: flex;
                    flex-direction: column;
                    width: 100%;
                    div.p-card-content {
                      // height: 80%;
                      .input_email {
                        margin-bottom: 1rem;
                        input {
                          width: 100%;
                        }
                      }
                      .input_password {
                        margin-bottom: 1rem;
                        > div {
                          width: 100%;
                          input {
                            width: 100%;
                          }
                        }
                      }
                      .Forgotten_password {
                        margin-bottom: 1rem;
                      }
                    }
                    div.p-card-footer {
                      display: flex;
                      justify-content: center;
                      align-items: center;
                    }
                  }
                }
              }
            }
            .voice_up,
            .voice_down,
            .power {
              content: '';
              position: absolute;
              height: 70px;
              width: 13px;
              background-color: #130e0e;
              border-radius: 5px;
              z-index: 7;
              //rotate: 90deg;
              -webkit-border-radius: 5px;
              -moz-border-radius: 5px;
              -ms-border-radius: 5px;
              -o-border-radius: 5px;
            }
            .voice_up {
              top: 10%;
              left: -13px;
            }
            .voice_down {
              top: 24%;
              left: -13px;
            }
            .power {
              top: 17%;
              right: -13px;
            }
            .sonser,
            .voice {
              position: absolute;
              z-index: 7;
            }
            .sonser {
              height: 15px;
              background-color: #130e0e;
              width: 33.33%;
              left: 33.33%;
              border-radius: 0 0 15px 15px;
            }
            .voice {
              height: 5px;
              background-color: #b3b0b0;
              width: 15%;
              left: 42.5%;
              border-radius: 15px;
              -webkit-border-radius: 15px;
              -moz-border-radius: 15px;
              -ms-border-radius: 15px;
              -o-border-radius: 15px;
            }
            .carme {
              content: '';
              position: absolute;
              height: 7px;
              width: 7px;
              top: -1px;
              left: calc(63% - 15px);
              background-color: #b3b0b0;
              border-radius: 50%;
              -webkit-border-radius: 50%;
              -moz-border-radius: 50%;
              -ms-border-radius: 50%;
              -o-border-radius: 50%;
              z-index: 10;
              display: none;
            }
          }
          .mobile_body_dark {
            border: 0.5rem solid #130e0e;
            border-radius: 32px;
            -webkit-border-radius: 32px;
            -moz-border-radius: 32px;
            -ms-border-radius: 32px;
            -o-border-radius: 32px;
            height: 100%;
            margin: auto;
            position: relative;
            position: relative;
            // screen and (max-width: 568px)
            // @include MediaQueries(Xxs) {}
            @include MediaQueries(Mobile) {
              &::after {
                content: '📱 568';
                position: absolute;
                top: 0%;
                left: 0px;
                border-radius: 0.5rem;
                z-index: 7;
                font-size: 20px;
                font-weight: bold;
                background-color: #130e0e;
                color: #fff;
                padding: 10px 15px;
              }
            }
            // screen and (min-width: 569px) and (max-width: 767px)
            // @include MediaQueries(Xs) {}
            @include MediaQueries(Tablet) {
              &::after {
                content: '📱 567 767';
                position: absolute;
                top: 0%;
                left: 0px;
                border-radius: 0.5rem;
                z-index: 7;
                font-size: 20px;
                font-weight: bold;
                background-color: #130e0e;
                color: #fff;
                padding: 10px 15px;
              }
            }
            // screen and (min-width: 768px) and (max-width: 991px)
            // @include MediaQueries(Md) {}
            @include MediaQueries(laptop) {
              &::after {
                content: '💻 768 991';
                position: absolute;
                top: 0%;
                left: 0px;
                border-radius: 0.5rem;
                z-index: 7;
                font-size: 20px;
                font-weight: bold;
                background-color: #130e0e;
                color: #fff;
                padding: 10px 15px;
              }
            }
            // screen and (min-width: 992px) and (max-width: 1199px)
            // @include MediaQueries(Lg) {}
            @include MediaQueries(laptopLg) {
              &::after {
                content: '💻➕ 992 1199';
                position: absolute;
                top: 0%;
                left: 0px;
                border-radius: 0.5rem;
                z-index: 7;
                font-size: 20px;
                font-weight: bold;
                background-color: #130e0e;
                color: #fff;
                padding: 10px 15px;
              }
            }
            // screen and (min-width: 1200px) and (max-width: 1399px)
            // @include MediaQueries(Xlg) {}
            @include MediaQueries(Desktop) {
              &::after {
                content: '🖥️ 1200 1399';
                position: absolute;
                top: 0%;
                left: 0px;
                border-radius: 0.5rem;
                z-index: 7;
                font-size: 20px;
                font-weight: bold;
                background-color: #130e0e;
                color: #fff;
                padding: 10px 15px;
                display: none;
              }
              width: 50%;
              overflow-x: hidden;
            }
            // screen and (min-width: 1400px)
            // @include MediaQueries(Xxlg) {}
            @include MediaQueries(DesktopLg) {
              &::after {
                content: '🖥️➕ 1400';
                position: absolute;
                top: 0%;
                left: 0px;
                border-radius: 0.5rem;
                z-index: 7;
                font-size: 20px;
                font-weight: bold;
                background-color: #130e0e;
                color: #fff;
                padding: 10px 15px;
                display: none;
              }
              width: 50%;
            }
            .mobile_content {
              position: relative;
              border-radius: 24px;
              -webkit-border-radius: 24px;
              -moz-border-radius: 24px;
              -ms-border-radius: 24px;
              -o-border-radius: 24px;
              border: 0.2rem solid #130e0e;
              height: 100%;
              background-color: #fff;
              padding: 1rem;
              display: flex;
              justify-content: space-between;
              align-items: center;
              form {
                height: 100%;
                display: flex;
                justify-content: space-between;
                align-items: center;
                width: 100%;
                .prime_card_form_signup {
                  border: none;
                  padding: 0;
                  margin: 0;
                  box-shadow: none;
                  height: 100%;
                  max-height: 100%;
                  overflow: hidden;
                  border-radius: 0px;
                  display: flex;
                  justify-content: center;
                  align-items: center;
                  div.p-card-header {
                    height: 20%;
                    width: 100%;
                    display: flex;
                    align-items: center;
                    width: 100%;
                  }
                  div.p-card-body {
                    padding: 0;
                    margin: 0;
                    margin-bottom: 1rem;
                    height: 80%;
                    display: flex;
                    flex-direction: column;
                    div.p-card-content {
                      height: 80%;
                      .prime_card_form_signup_content {
                        > div {
                          display: flex;
                          flex-direction: column;
                          justify-content: space-between;
                          > div {
                            margin-top: 1rem;
                          }
                        }
                      }
                    }
                    div.p-card-footer {
                      height: 20%;
                      display: flex;
                      justify-content: center;
                      align-items: center;
                    }
                  }
                }
                .prime_card_form_login {
                  border: none;
                  padding: 0;
                  margin: 0;
                  box-shadow: none;
                  height: 100%;
                  max-height: 100%;
                  overflow: hidden;
                  border-radius: 0px;
                  display: flex;
                  justify-content: center;
                  align-items: center;
                  width: 100%;
                  div.p-card-header {
                    height: 20%;
                    width: 100%;
                    display: flex;
                    align-items: center;
                    width: 100%;
                  }
                  div.p-card-body {
                    padding: 0;
                    margin: 0;
                    margin-bottom: 1rem;
                    height: 80%;
                    display: flex;
                    flex-direction: column;
                    width: 100%;
                    div.p-card-content {
                      // height: 80%;
                      .input_email {
                        margin-bottom: 1rem;
                        input {
                          width: 100%;
                        }
                      }
                      .input_password {
                        margin-bottom: 1rem;
                        > div {
                          width: 100%;
                          input {
                            width: 100%;
                          }
                        }
                      }
                      .Forgotten_password {
                        margin-bottom: 1rem;
                      }
                    }
                    div.p-card-footer {
                      display: flex;
                      justify-content: center;
                      align-items: center;
                    }
                  }
                }
              }
            }
            .voice_up,
            .voice_down,
            .power {
              content: '';
              position: absolute;
              height: 70px;
              width: 13px;
              background-color: #130e0e;
              border-radius: 5px;
              z-index: 7;
              //rotate: 90deg;
              -webkit-border-radius: 5px;
              -moz-border-radius: 5px;
              -ms-border-radius: 5px;
              -o-border-radius: 5px;
            }
            .voice_up {
              top: 10%;
              left: -13px;
            }
            .voice_down {
              top: 24%;
              left: -13px;
            }
            .power {
              top: 17%;
              right: -13px;
            }
            .sonser,
            .voice {
              position: absolute;
              z-index: 7;
            }
            .sonser {
              height: 15px;
              background-color: #130e0e;
              width: 33.33%;
              left: 33.33%;
              border-radius: 0 0 15px 15px;
            }
            .voice {
              height: 5px;
              background-color: #b3b0b0;
              width: 15%;
              left: 42.5%;
              border-radius: 15px;
              -webkit-border-radius: 15px;
              -moz-border-radius: 15px;
              -ms-border-radius: 15px;
              -o-border-radius: 15px;
            }
            .carme {
              content: '';
              position: absolute;
              height: 7px;
              width: 7px;
              top: -1px;
              left: calc(63% - 15px);
              background-color: #b3b0b0;
              border-radius: 50%;
              -webkit-border-radius: 50%;
              -moz-border-radius: 50%;
              -ms-border-radius: 50%;
              -o-border-radius: 50%;
              z-index: 10;
              display: none;
            }
          }
        }
      }
    }
  }
}
</style>
