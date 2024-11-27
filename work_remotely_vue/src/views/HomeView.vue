<script setup>
import axios from 'axios'
</script>

<template>
  <main>
    <div class="wrapper_website_work_remotely">
      <div class="container mx-auto">
        <!--  -->
        <div class="top_title my-4 px-4">
          <div class="flex justify-between items-center">
            <!-- Form -->
            <div class="">
              <div class="card flex justify-center">
                <prime_button label="Create Website" @click="visibleFormCreateWebsites = true" />
                <prime_dialog
                  v-model:visible="visibleFormCreateWebsites"
                  modal
                  header="Create Websites"
                  :style="{ width: '80%' }"
                >
                  <form class="form_website_create" enctype="multipart/form-data">
                    <span class="text-surface-500 dark:text-surface-400 block mb-8"
                      >Adding Website information.</span
                    >
                    <!-- 1️⃣ Name -->
                    <div class="flex items-center gap-4 mb-4">
                      <label for="websiteName" class="font-semibold w-40">Website Name</label>
                      <prime_input_text
                        id="websiteName"
                        class="flex-auto"
                        autocomplete="off"
                        v-model="formCreateWebsites.name"
                      />
                    </div>
                    <!-- 2️⃣ Url -->
                    <div class="flex items-center gap-4 mb-4">
                      <label for="websiteUrl" class="font-semibold w-40">Website Url</label>
                      <prime_input_text
                        id="websiteUrl"
                        class="flex-auto"
                        autocomplete="off"
                        v-model="formCreateWebsites.url"
                      />
                    </div>
                    <!-- 3️⃣ Details -->
                    <div class="flex items-center gap-4 mb-4">
                      <label for="websiteDetails" class="font-semibold w-40">Website Details</label>
                      <prime_textarea
                        id="websiteDetails"
                        class="flex-auto"
                        autocomplete="off"
                        v-model="formCreateWebsites.details"
                      />
                    </div>
                    <!-- 4️⃣ Website Type -->
                    <div class="flex items-center gap-4 mb-4">
                      <div class="w-40">
                        <p class="font-semibold">Website Type</p>
                      </div>
                      <div class="flex flex-col md:flex-row gap-2">
                        <prime_input_group>
                          <prime_radio_button
                            v-model="formCreateWebsites.website_type"
                            inputId="ingredient1"
                            name="website_type"
                            value="services"
                          />
                          <label for="ingredient1" class="ml-2"> Services </label>
                        </prime_input_group>
                        <prime_input_group>
                          <prime_radio_button
                            v-model="formCreateWebsites.website_type"
                            inputId="ingredient2"
                            name="website_type"
                            value="templates"
                          />
                          <label for="ingredient2" class="ml-2"> Templates </label>
                        </prime_input_group>
                        <prime_input_group>
                          <prime_radio_button
                            v-model="formCreateWebsites.website_type"
                            inputId="ingredient3"
                            name="website_type"
                            value="employment"
                          />
                          <label for="ingredient3" class="ml-2"> Employment </label>
                        </prime_input_group>
                      </div>
                    </div>
                    <!-- emo Website Language -->
                    <div class="flex items-center gap-4 mb-4">
                      <div class="w-40">
                        <p class="font-semibold">Website Language</p>
                      </div>
                      <div class="flex flex-col md:flex-row gap-2">
                        <prime_input_group>
                          <prime_radio_button
                            v-model="formCreateWebsites.website_language"
                            inputId="ingredient2"
                            name="website_language"
                            value="english"
                          />
                          <label for="ingredient2" class="ml-2"> English </label>
                        </prime_input_group>
                        <prime_input_group>
                          <prime_radio_button
                            v-model="formCreateWebsites.website_language"
                            inputId="ingredient3"
                            name="website_language"
                            value="arabic"
                          />
                          <label for="ingredient3" class="ml-2"> Arabic </label>
                        </prime_input_group>
                      </div>
                    </div>
                    <!--  Image  -->
                    <div class="flex items-center gap-4 mb-4">
                      <label for="websiteImage" class="font-semibold w-40">Website Image</label>
                      <prime_file_upload
                        type="file"
                        ref="file"
                        :multiple="true"
                        name="demo[]"
                        @select="handleImageFileUpload"
                        accept="image/*"
                        :maxFileSize="1000000"
                      >
                        <template #empty>
                          <span>Drag and drop files to here to upload.</span>
                        </template>
                      </prime_file_upload>
                    </div>
                    <!-- Buttons -->
                    <div class="flex justify-end gap-2">
                      <prime_button
                        type="button"
                        label="Cancel"
                        severity="secondary"
                        @click="visibleFormCreateWebsites = false"
                      ></prime_button>
                      <prime_button
                        type="button"
                        label="Save"
                        @click.prevent="website_create"
                      ></prime_button>
                    </div>
                  </form>
                </prime_dialog>
              </div>
            </div>
            <!-- Website Count  -->
            <prime_button
              type="button"
              label="All Websites"
              icon="pi pi-list-check"
              :badge="websites.length"
              badgeSeverity="contrast"
              outlined
            />
          </div>
        </div>
        <div class="inner_website_work_remotely">
          <div
            class="xs_grid_12 sm_grid_12 md_grid_12 lg_grid_12 xlg_grid_12 xxlg_grid_12 p-4 gap_10"
          >
            <div
              class="xsm_item_12 sm_item_6 md_item_4 lg_item_3 xlg_item_3 xxlg_item_2 hover:shadow-lg rounded-2xl p-2 my-4"
              style="width: 100%; overflow: hidden"
              v-for="website in websites"
              :key="website"
            >
              <!-- Start Card -->
              <prime_card
                style="overflow: hidden; border-radius: none; box-shadow: none"
                class="animate__animated animate__backInDown"
              >
                <template #header>
                  <img alt="user header" :src="website.get_image" class="w-full h-64" />
                </template>
                <template #title>
                  <div class="flex justify-between">
                    <h2 class="text-2xl font-bold capitalize">{{ website.name }}</h2>
                    <prime_tag severity="success" :value="website.website_language" />
                  </div>
                </template>
                <template #subtitle>
                  <!-- <p>{{ website.details }}</p> -->
                </template>
                <template #content>
                  <p class="m-0 pb-4" dir="auto">{{ website.details }}</p>
                </template>
                <template #footer>
                  <div class="flex gap-1 mt-1">
                    <prime_button
                      :label="website.website_type"
                      :severity="getSeverity(website.website_type)"
                      class="w-full capitalize"
                    />
                    <prime_button class="w-full">
                      <a :href="website.url" target="_blank">View</a>
                    </prime_button>
                  </div>
                </template>
              </prime_card>
              <!-- End Card -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  name: 'HomeView',
  data() {
    return {
      websites: [],
      // For Form
      visibleFormCreateWebsites: false,
      formCreateWebsites: {
        name: '',
        details: '',
        url: '',
        website_type: '',
        website_language: '',
      },
      selectedImageFile: null,
      errorsInCreate: [],
    }
  },
  mounted() {
    document.title = 'Home'
    this.getWebsiteList()
  },
  methods: {
    getWebsiteList() {
      axios
        .get('api/website/website_list')
        .then((response) => {
          this.websites = response.data
          console.log('this.websites: ', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getSeverity(type) {
      if (type === 'services') {
        return 'success'
      } else if (type === 'templates') {
        return 'danger'
      } else if (type === 'employment') {
        return 'help'
      }
      return 'secondary' // إذا كانت القيمة غير محددة، يمكن إرجاع قيمة فارغة
    },
    // For Send Data
    // For Upload Image to Post Store and for Post
    handleImageFileUpload(event) {
      // let file = event.target.files[0]
      // يمكن الحصول على الملفات من event.files
      const file = event.files ? event.files[0] : null

      if (file) {
        console.log('file: ', file)
        this.selectedImageFile = file
        console.log('FormData contains image:', this.selectedImageFile.name)
        // Send Image to View
        this.$toast.add({
          severity: 'success',
          summary: `Data contains image`,
          detail: `${this.selectedImageFile.name}`,
          life: 3000,
        })
      } else {
        console.log('No file selected.')
      }
    },
    async website_create() {
      this.errorsInCreate = []
      const formData = new FormData()
      // Name
      if (this.formCreateWebsites.name == '') {
        this.$toast.add({
          severity: 'error',
          summary: 'Type Website Name',
          detail: 'Your Website Name is missing',
          life: 3000,
        })
        this.errorsInCreate.push('Type Script Title')
      } else if (this.formCreateWebsites.name !== '') {
        formData.append('name', this.formCreateWebsites.name)
      }
      // Url
      if (this.formCreateWebsites.url == '') {
        this.$toast.add({
          severity: 'error',
          summary: 'Type Website Url',
          detail: 'Your Website Url is missing',
          life: 3000,
        })
        this.errorsInCreate.push('Type Script Title')
      } else if (this.formCreateWebsites.url !== '') {
        formData.append('url', this.formCreateWebsites.url)
      }
      // details
      if (this.formCreateWebsites.details !== '') {
        formData.append('details', this.formCreateWebsites.details)
      }
      // website_type
      if (this.formCreateWebsites.website_type !== '') {
        formData.append('website_type', this.formCreateWebsites.website_type)
      }
      // website_language
      if (this.formCreateWebsites.website_language !== '') {
        formData.append('website_language', this.formCreateWebsites.website_language)
      }
      // Add Image [  ] إضافة الصور إذا تم تحديدها
      if (this.selectedImageFile) {
        formData.append('image', this.selectedImageFile)
      }
      // ✅ All Is Good
      if (this.errorsInCreate.length === 0) {
        await axios
          .post('api/website/website_create/', formData, {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          })
          .then((response) => {
            this.getWebsiteList()
            this.formCreateWebsites.name = ''
            this.formCreateWebsites.url = ''
            this.formCreateWebsites.details = ''
            this.formCreateWebsites.website_type = ''
            this.formCreateWebsites.selectedImageFile = null

            console.log('Data Is Send To Django: ', response.data)
            this.$toast.add({
              severity: 'success',
              summary: 'Website created',
              detail: 'Website created successfully.',
              life: 3000,
            })
            this.visibleFormCreateWebsites = false
          })
      }
    },
  },
}
</script>
