<template>
  <div class="q-pa-sm">
    <q-card class="row q-flex justify-center">
      <h6>this is master branch </h6>
      <div class="col-12  col-md-8 q-px-md q-pt-md text-center " style="color: rgb(7, 112, 112);">
        <div class="text-h5 text-bold">200,342.00</div>
        <div class="text-subtitle2 text-grey">Current Balance</div>
      </div>

        <div class="row text-center">
          <q-card-section class="">
          <div class="text-body4 text-bold">200,342.00</div>
          <div class="text-subtitle1 text-grey"> <q-icon name="add" color="yellow" class="bg-green"/>income</div>
          </q-card-section>
          <q-card-section class="">
          <div class="text-body4 text-bold">200,342.00</div>
          <div class="text-subtitle1 text-grey"> <q-icon name="add" color="yellow" class="bg-green"/>Pre-Balance</div>
          </q-card-section>
          <q-card-section class="">
          <div class="text-body4 text-bold">200,342.00</div>
          <div class="text-subtitle1 text-grey"> <q-icon name="add" color="yellow" class="bg-red"/>Expense</div>
          </q-card-section>

        </div>
    </q-card>

      <q-card class="col-md-12 my-card q-my-md">
      <q-card-actions align="around">
        <q-btn flat class="text-capitalize"  @click="showIncomeComponent" icon="add" >Add income</q-btn>
        <q-btn flat class="text-capitalize" @click="showExpenseComponent" icon="add">Add Expense</q-btn>
      </q-card-actions>
      <div v-if="showIncome">
      <income/>
    </div>
    <div v-if="showExpense">
      <expense/>
    </div>
    </q-card>

    <q-card class="col-sm-12 text-center my-card q-my-sm">
      <!-- <q-list class="" >
        <q-item class="row">
          <q-item-section class="" align="around" >
            <div class="text-body1">Recent Expenses</div>
            <div class="text-subtitle2">Totol expenses: 23,3200</div>
        </q-item-section>
       </q-item>
      </q-list> -->

      <q-expansion-item v-model="expansionItem"
      class="no-icon-expansion bg-grey-3"
        label="Account settings"
        caption="John Doe"
                        >
        <template v-slot:header>
          <q-item-section avatar>
            <q-avatar>
              <img src="~src\assets\umar.png">
            </q-avatar>
          </q-item-section>
          <q-item-section class="items-start" align="around" style="width: 150px;">
            <div class="text-bold float-left">27 Jun 2022 </div>
            <!-- <div>Food</div> -->
          </q-item-section>

         <q-item-section class="items-end float-left">
            <div class="text-bold" style="color: crimson;">23200 Inc <q-icon class="text-bold" name="call_made" /></div>
            <div  style="color:rgb(125, 199, 15)">34340 Exp <q-icon class="text-bold" name="call_received" /></div>
          </q-item-section>

          <!-- <q-icon name="more_vert" size="1.5rem" class="text-center q-pt-sm q-ml-md" v-ripple>
              <q-menu stop-propagation switch-toggle-side>
                <q-list style="min-width: 100px">
                  <q-item clickable v-close-popup>
                    <q-item-section>New tab</q-item-section>
                  </q-item>
                </q-list>
              </q-menu>
            </q-icon> -->
        </template>

          <q-card-section>
            <q-separator class="" color="cyan-8" size="2px"/>

                <div class="row justify-between" >
                  <div class="col-4" style="width: 200px;">
                    doodh or dahi alnsd jlasd
                  </div>
                  <div class="col-4 q-pl-xl">
                    239
                  </div>
                </div>

                <div class="row justify-between" >
                  <div class="col-4" style="width: 200px;">
                    doodh or dahi alnsd jlasd
                  </div>
                  <div class="col-4 q-pl-xl">
                    239
                  </div>
                </div>
                <div class="row justify-between" >
                  <div class="col-4" style="width: 200px;">
                    doodh or dahi alnsd jlasd
                  </div>
                  <div class="col-4 q-pl-xl">
                    239
                  </div>
                </div>
                <div class="row justify-between" >
                  <div class="col-4" style="width: 200px;">
                    doodh or dahi alnsd jlasd
                  </div>
                  <div class="col-4 q-pl-xl">
                    239
                  </div>
                </div>
            </q-card-section>
      </q-expansion-item>

      <!-- <q-list class="bg-grey-3 text-bold text-grey-10 shadow-2 rounded-borders">
        <q-item class="row">
          <q-item-section class="row" avatar>
            <q-avatar>
              <img src="~src\assets\shahwazir.png">
            </q-avatar>
          </q-item-section>

          <q-item-section class="items-start" align="around" style="width: 150px;">
            <div class="float-left">27 Jun 2022 Monday</div>
            <div>Food</div>
          </q-item-section>

          <q-item-section class="items-end float-left">
            <div class="text-bold" style="color: crimson;">23200 Inc <q-icon class="text-bold" name="call_made" /></div>
            <div  style="color:rgb(125, 199, 15)">34340 Exp <q-icon class="text-bold" name="call_received" /></div>
          </q-item-section>
        </q-item>

        <q-separator color="grey-10" size="2px" />
      </q-list>

      <q-list class="bg-grey-3   text-bold text-grey-10 shadow-2 rounded-borders">
        <q-item class="row">
          <q-item-section class="row" avatar>
            <q-avatar>
              <img src="~src\assets\umarkhan.jpeg">
            </q-avatar>
          </q-item-section>

          <q-item-section class="items-start" align="around" style="width: 150px;">
            <div class="float-left">27 Jun 2022 Monday</div>
            <div>Traveling</div>
          </q-item-section>

          <q-item-section class="items-end float-left">
            <div class="text-bold" style="color: crimson;">23200 Inc <q-icon class="text-bold" name="call_made" /></div>
            <div  style="color:greenyellow">34340 Exp <q-icon class="text-bold" name="call_received" /></div>
          </q-item-section>
        </q-item>

        <q-separator dark />
      </q-list> -->

      <div v-if="showIncome">
      <income/>
    </div>
    <div v-if="showExpense">
      <expense/>
    </div>
    </q-card>

  </div>
</template>
<script>
import income from '../pages/components/income.vue'
import expense from '../pages/components/expense.vue'
export default {
  components:{
   income,
   expense,
  },
  data() {
    return {
      showIncome: false,
      showExpense: false,

    };
  },
  methods: {
    showIncomeComponent() {
      this.showIncome = !this.showIncome;
      this.showExpense = false;
    },
    showExpenseComponent(){
      this.showExpense = !this.showExpense;
      this.showIncome = false;

    }

  },
  mounted() {

  },
};
</script>
