
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/home.vue') },
      { path: 'logout', component: () => import('pages/Authentication/logout.vue') },
      { path: 'signUp', component: () => import('pages/Authentication/signUp.vue') },
      { path: 'login', component: () => import('pages/Authentication/login.vue') },
      { path: 'table', component: () => import('pages/AddUser.vue') },
      { path: 'index', component: () => import('pages/IndexPage.vue') },
      { path: 'Report', component: () => import('pages/Report.vue') },
      { path: 'setting', component: () => import('pages/setting.vue') },
      // { path: 'Income', component: () => import('pages/components/Income.vue') },

    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
