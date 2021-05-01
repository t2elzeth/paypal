<template>
  <div>
    <template v-if="!loading">
      <form action="https://www.sandbox.paypal.com/cgi-bin/webscr" method="post">
        <input type="hidden" name="cmd" value="_xclick" id="id_cmd">
        <input type="hidden" name="charset" value="utf-8" id="id_charset">
        <input type="hidden" name="currency_code" :value="serverData.currency_code" id="id_currency_code">
        <input type="hidden" name="no_shipping" value="1" id="id_no_shipping">
        <input type="hidden" name="business" :value="serverData.business" id="id_business">
        <input type="hidden" name="amount" :value="serverData.amount" id="id_amount">
        <input type="hidden" name="item_name" :value="serverData.item_name" id="id_item_name">
        <input type="hidden" name="invoice" :value="serverData.invoice" id="id_invoice">
        <input type="hidden" name="notify_url" value="http://127.0.0.1:8001/paypal/" id="id_notify_url">
        <input type="hidden" name="cancel_return" value="http://127.0.0.1:8080/payment-cancelled/"
               id="id_cancel_return">
        <input type="hidden" name="return" value="http://127.0.0.1:8080/payment-done/" id="id_return">
        <input type="image" src="https://www.paypal.com/en_US/i/btn/btn_buynowCC_LG.gif" name="submit" alt="Buy it Now">
      </form>
    </template>
    <template v-else>
      Loading
    </template>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "BuyPremium",
  data() {
    return {
      serverData: Object,
      loading: true,
    }
  },
  methods: {
    async getServerData() {
      axios.post("http://127.0.0.1:8001/buy_premium/")
           .then(res => {
             console.log(res.data)
             this.serverData = res.data
           })
           .catch(err => console.log(err))
    },
  },
  async created() {
    await this.getServerData()
    this.loading = false
  }
}
</script>

<style scoped>

</style>