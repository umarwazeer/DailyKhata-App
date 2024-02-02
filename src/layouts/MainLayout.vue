<template>
  <q-layout view="lHh Lpr lFf" color="red" class="bg-cyan-9">
    <q-header elevated class="bg-cyan-9">
      <q-toolbar class="bg-cyan-9">
        <q-btn
          flat
          dense
          round
          icon="arrow_back_ios"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>
          Daily Khata
        </q-toolbar-title>

        <!-- <div>Quasar v{{ $q.version }}</div> -->
        <q-btn flat @click="logout" >

        <q-icon name="power_settings_new"></q-icon>
      </q-btn>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      :width="200"
      bordered
    >
      <q-list>
        <q-item-section class="items-center q-mt-lg">
  <q-avatar size="67px" class="text bordered-2" bordered font-size="22px" color="teal" text-color="white" >
    <q-img src="~assets/umar.png"></q-img>
  </q-avatar>
</q-item-section>
        <q-item-label class="text-center q-pt-md" >
          Umar Khan
      </q-item-label>

      <q-item-label class="text-center " >
          a4umakhan@gmail.com
      </q-item-label>


        <EssentialLink class="q-pt-md"
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from 'vue'
import EssentialLink from 'components/EssentialLink.vue'

const linksList = [
  {
    title: 'Home',
    caption: 'Homepage',
    icon: 'home',
    to: '/'
  },
  {
    title: 'Add Users',
    caption: 'Add your new User',
    icon: 'manage_search',
    to: 'table'
  },
  {
    title: 'Reports',
    caption: 'Your Reports',
    icon: 'summarize',
    to: 'Report'
  },
  {
    title: 'Setting',
    caption: 'Manage Your Setting',
    icon: 'settings',
    to: 'setting'
  },
  {
    title: 'Logout',
    caption: 'Logout now',
    icon: 'logout',
    to: 'logout'
  }
]

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink
  },
  methods:{
    logout () {
      this.$q.dialog({
        title: 'Confirm',
        message: 'You want shure to logut now!',
        cancel: true,
        persistent: true
      }).onOk(() => {
       this.$router.push('logout')
        console.log('>>>> OK')
      }).onOk(() => {
        // console.log('>>>> second OK catcher')
      }).onCancel(() => {
        // console.log('>>>> Cancel')
      }).onDismiss(() => {
        // console.log('I am triggered on both OK and Cancel')
      })
    },
  },

  setup () {
    const leftDrawerOpen = ref(false)

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  }
})
</script>
