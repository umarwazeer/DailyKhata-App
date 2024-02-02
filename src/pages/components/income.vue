<template>
  <div class="row q-pa-sm">
    <div class="col  q-gutter-y-md q-pa-sm">
      <q-input filled dense v-model="date" mask="date" :rules="['date']">
      <template v-slot:append>
        <q-icon name="event" class="cursor-pointer">
          <q-popup-proxy ref="qDateProxy" transition-show="scale" transition-hide="scale">
            <q-date v-model="date">
              <div class="row items-center justify-end">
                <q-btn v-close-popup label="Close" color="primary" flat />
              </div>
            </q-date>
          </q-popup-proxy>
        </q-icon>
      </template>
    </q-input>
    <q-input type="price" label="add Income" outlined dense><q-icon name="calculate"  size="2rem" class="q-pt-xs"/>
</q-input>
      <q-select
        filled
        v-model="Incomecategery"
        use-input
        input-debounce="0"
        label="Choose Income Categery"
        :options="options"
        @filter="filterFn"
        behavior="menu"
      >
        <template v-slot:no-option>
          <q-item>
            <q-item-section class="text-grey">
              No results
            </q-item-section>
          </q-item>
        </template>
      </q-select>
      <q-input type="price"  label="write your comment" outlined dense><q-icon name="calculator"/></q-input>
      <q-btn  class="text-subtitle1 text-bold full-width" dense color="cyan" >Add Income</q-btn>
    </div>

  </div>

</template>

<script >
const stringOptions = [
  'education', 'clothing', 'fruit', 'travel', 'snakes', 'bills'
]

export default {
  // Your component logic here
  data(){
    return{
      date: '2019/02/01',
      Incomecategery: null,
      stringOptions,
      options: stringOptions
    }
  },
  methods: {
    filterFn (val, update) {
      if (val === '') {
        update(() => {
          this.options = stringOptions
        })
        return
      }

      update(() => {
        const needle = val.toLowerCase()
        this.options = stringOptions.filter(v => v.toLowerCase().indexOf(needle) > -1)
      })
    }
  }
};
</script>
