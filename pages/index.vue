<template>
  <section class="container">
    <section class="hero">
      <div class="hero-body container">
        <div class="container">
          <h1 class="title">
            Are you a Customer or a Courier?
          </h1>
        </div>
      </div>
    </section>
    <nav class="level is-mobile">
      <div class="level-item has-text-centered"></div>
      <div class="level-item has-text-centered">
        <b-button tag="router-link"
          to="/customer"
          type="is-info" rounded outlined expanded>
            Customer
        </b-button>
      </div>
      <div class="level-item has-text-centered">
        <b-button tag="router-link"
          to="/courier"
          type="is-info" rounded outlined expanded>
            Courier
        </b-button>
      </div>
      <div class="level-item has-text-centered"></div>
    </nav>
  </section>
</template>

<script>
import Card from '~/components/Card'

export default {
  name: 'HomePage',

  components: {
    Card
  }
}
</script>
