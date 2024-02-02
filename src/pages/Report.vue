<template>
  <div class="q-py-sm">
    <div class="q-gutter-y-md">
        <!-- <q-expansion-item
        icon="perm_identity"
        label="Account settings"
      >
            <q-date
            style="width: 500px;"
      v-model="date"
    />
      </q-expansion-item> -->

      <q-card>
        <q-tabs
          v-model="tab"
          dense
          class="text-grey"
          active-color="primary"
          indicator-color="primary"
          align="justify"
          narrow-indicator
        >
          <q-tab name="mails" label="Daily" />
          <q-tab name="alarms" label="Weekly" />
          <q-tab name="movies" label="Calander" />
          <q-tab name="movies" label="Monthly" />
        </q-tabs>

        <q-separator  color="cyan-9" size="2px"/>

        <q-tab-panels v-model="tab" animated>
          <q-tab-panel name="mails">

      <q-input filled dense v-model="date" mask="##/##/####" label="Select Date " :rules="[checkDate]">
      <template v-slot:append>
        <q-icon name="event" class="cursor-pointer">
          <q-popup-proxy ref="qDateProxy" transition-show="scale" transition-hide="scale">
            <q-date v-model="date" emit-immediately @update:model-value="onUpdateMv" :key="dpKey" minimal mask="MM/DD/YYYY">
            <q-btn type="submit" label="close" icon="clo" color="primary" v-close-popup/>

            </q-date>
          </q-popup-proxy>

        </q-icon>
      </template>
    </q-input>

    <q-expansion-item
    v-model="expansionItem"
    dense
    class="no-icon-expansion"
    label="Account settings"
    caption="John Doe"
                        >
        <template v-slot:header>
          <div class="text-h5 q-py-sm  text-cyan-8" style="margin-left: 0px; padding-left: 0px;">27</div>
        <div class="text-h6 text-body1" style="padding:12px 10px ;"> Jun 2023</div>


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

          <q-card-section bordered>

            <q-separator class="q-mb-sm" color="cyan-8" size="2px"/>

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

            <div class="row justify-between" >
              <div class="col-4" style="width: 200px;">
                doodh or dahi alnsd jlasd
              </div>
               <div class="col-4 q-pl-xl">
                239
               </div>
            </div>

            <div class="row justify-between" >
              <div class="col-4">
                29 Des Friday
              </div>

               <div class="col-4 q-pl-xl">
                23,200
               </div>
            </div>

            <q-separator class="q-my-sm" color="cyan-8" size="2px"/>

            <div class="row justify-between" >
              <div class="col-4">
                29 Des Friday
              </div>

              <div class="col-4 q-pl-xl">
               income: 2340
               </div>

               <div class="col-4 q-pl-xl">
                total: 23,200
               </div>
            </div>
          </q-card-section>
      </q-expansion-item>

      <!------------------just new ------------------>
    <q-card class="" flat bordered dense>
      <!-- <q-img
        src="https://cdn.quasar.dev/img/parallax2.jpg"
      />

      <q-card-section>
        <div class="text-overline text-orange-9">Overline</div>
        <div class="text-h5 q-mt-sm q-mb-xs">Title</div>
        <div class="text-caption text-grey">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </div>
      </q-card-section> -->

      <q-card-actions style="width:340px;" clickable class="">
        <div class="text-h5  text-cyan-8">27</div>
        <div class="text-h6 text-body1 q-pl-sm"> Jun 2023</div>
        <q-item-section class="items-end float-left">
            <div class="text-bold" style="color: crimson;">23300 <q-icon class="text-bold" name="call_made" /></div>
            <div  style="color:rgb(125, 199, 15)">34340<q-icon class="text-bold" name="call_received" /></div>
          </q-item-section>
        <!-- <q-btn flat color="primary" label="Bookaada" /> -->

        <q-space />

        <q-btn
          color="grey"
          round
          flat
          dense
          :icon="expanded ? 'keyboard_arrow_down' : 'keyboard_arrow_right'"
          @click="expanded = !expanded"
        />
      </q-card-actions>

      <q-slide-transition>
        <div v-show="expanded">
          <q-separator />
            <q-card-section class="justify-between">
            <!-- <div class="row justify-between " >
              <div class="col-4">
                29 Des Friday
              </div>
              <div class="">
               Income 23230
               </div>
               <q-card-section class="row q-gutter-sm">
                <div class="">
                Expense
               </div>
               <div class="">
                Expense
               </div>
               </q-card-section>

            </div> -->
            <q-separator class="q-mb-sm"  color="cyan-8" size="2px"/>

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

            <div class="row justify-between" >
              <div class="col-4" style="width: 200px;">
                doodh or dahi alnsd jlasd
              </div>
               <div class="col-4 q-pl-xl">
                239
               </div>
            </div>

            <div class="row justify-between" >
              <div class="col-4">
                29 Des Friday
              </div>

               <div class="col-4 q-pl-xl">
                23,200
               </div>
            </div>

            <q-separator class="q-my-sm" color="cyan-8" size="2px"/>

            <div class="row justify-between" >
              <div class="col-4">
                29 Des Friday
              </div>

              <div class="col-4 q-pl-xl">
               income: 2340
               </div>

               <div class="col-4 q-pl-xl">
                total: 23,200
               </div>
            </div>
          </q-card-section>
        </div>
      </q-slide-transition>
    </q-card>
  <!----------------------just new----------------------->

      <q-card class="q-mt-sm" flat bordered>
        <q-card-section class="justify-between" style="align-content:end;">
            <div class="row justify-between " >
              <!-- <div class="col-4">
                29 Des Friday
              </div> -->
              <div class="">
               Income 23230
               </div>
               <q-card-section class="row q-gutter-sm">
                <div class="">
                Expense
               </div>
               <div class="">
                Expense
               </div>
               </q-card-section>

            </div>
            <q-separator class="q-mb-sm" color="cyan-8" size="2px"/>

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

            <div class="row justify-between" >
              <div class="col-4" style="width: 200px;">
                doodh or dahi alnsd jlasd
              </div>
               <div class="col-4 q-pl-xl">
                239
               </div>
            </div>

            <div class="row justify-between" >
              <div class="col-4">
                29 Des Friday
              </div>

               <div class="col-4 q-pl-xl">
                23,200
               </div>
            </div>

            <q-separator class="q-my-sm" color="cyan-8" size="2px"/>

            <div class="row justify-between" >
              <div class="col-4">
                29 Des Friday
              </div>

              <div class="col-4 q-pl-xl">
               income: 2340
               </div>

               <div class="col-4 q-pl-xl">
                total: 23,200
               </div>
            </div>
          </q-card-section>
          </q-card>

          <q-card class="q-pa-sm  q-mt-sm">
            <div class="row justify-between q-py-xs text-body1" >
              <div class="col-4">
                29 Des Friday
              </div>
              <div class="col-4q-pl-md">
               Income 23230
               </div>
               <div class="col-4 q-pl-xl">
                Expense
               </div>
            </div>
            <q-separator class="q-mb-sm" color="cyan-8" size="2px"/>

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

            <div class="row justify-between" >
              <div class="col-4" style="width: 200px;">
                doodh or dahi alnsd jlasd
              </div>
               <div class="col-4 q-pl-xl">
                239
               </div>
            </div>

            <div class="row justify-between" >
              <div class="col-4">
                29 Des Friday
              </div>

               <div class="col-4 q-pl-xl">
                23,200
               </div>
            </div>

            <q-separator class="q-my-sm" color="cyan-8" size="2px"/>

            <div class="row justify-between" >
              <div class="col-4">
                29 Des Friday
              </div>

              <div class="col-4 q-pl-xl">
               income: 2340
               </div>

               <div class="col-4 q-pl-xl">
                total: 23,200
               </div>
            </div>

          </q-card>

          </q-tab-panel>

          <q-tab-panel name="alarms">
            <!-- <q-card class="col-sm-12 ">
      <q-card-actions align="around">
        <q-btn flat class="text-capitalize" @click="showExpenseComponent" icon="add">Add Expense</q-btn>
      </q-card-actions>
    </q-card> -->
    <!-- <div class="q-gutter-md">
      <div class="">
        Month Picker Model: {{date}}<br>
        <q-date v-model="date"   emit-immediately @update:model-value="onUpdateMv" :key="dpKey" minimal mask="MM" class="myDate"></q-date>
      </div>
      </div> -->
      <q-card class="q-pa-sm ">
            <div class="row justify-between q-py-xs text-body1" >
              <div class="col-4">
                29 Des Friday
              </div>
              <div class="col-4q-pl-md">
               Income 23230
               </div>
               <div class="col-4 q-pl-xl">
                Expense
               </div>
            </div>
            <q-separator class="q-mb-sm" color="cyan-8" size="2px"/>

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

            <div class="row justify-between" >
              <div class="col-4" style="width: 200px;">
                doodh or dahi alnsd jlasd
              </div>
               <div class="col-4 q-pl-xl">
                239
               </div>
            </div>

            <div class="row justify-between" >
              <div class="col-4">
                29 Des Friday
              </div>

               <div class="col-4 q-pl-xl">
                23,200
               </div>
            </div>

            <q-separator class="q-my-sm" color="cyan-8" size="2px"/>

            <div class="row justify-between" >
              <div class="col-4">
                29 Des Friday
              </div>

              <div class="col-4 q-pl-xl">
               income: 2340
               </div>

               <div class="col-4 q-pl-xl">
                total: 23,200
               </div>
            </div>

          </q-card>

          <q-card class="q-pa-sm ">
            <div class="row justify-between q-py-xs text-body1" >
              <div class="col-4">
                29 Des Friday
              </div>
              <div class="col-4q-pl-md">
               Income 23230
               </div>
               <div class="col-4 q-pl-xl">
                Expense
               </div>
            </div>
            <q-separator class="q-mb-sm" color="cyan-8" size="2px"/>

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

            <div class="row justify-between" >
              <div class="col-4" style="width: 200px;">
                doodh or dahi alnsd jlasd
              </div>
               <div class="col-4 q-pl-xl">
                239
               </div>
            </div>

            <div class="row justify-between" >
              <div class="col-4">
                29 Des Friday
              </div>

               <div class="col-4 q-pl-xl">
                23,200
               </div>
            </div>

            <q-separator class="q-my-sm" color="cyan-8" size="2px"/>

            <div class="row justify-between" >
              <div class="col-4">
                29 Des Friday
              </div>

              <div class="col-4 q-pl-xl">
               income: 2340
               </div>

               <div class="col-4 q-pl-xl">
                total: 23,200
               </div>
            </div>

          </q-card>

          </q-tab-panel>

          <q-tab-panel name="movies">
            <div class="text-h6">Movies</div>
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
          </q-tab-panel>
        </q-tab-panels>
      </q-card>

    </div>
  </div>
</template>
<script>
import { ref } from 'vue'

export default {
  data() {
    return {
      expanded: false,
      tab: 'mails',
      date: ref('2019/02/01')

    }
  }
}
</script>
