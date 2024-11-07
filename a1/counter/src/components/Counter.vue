<script setup>
    import { ref } from 'vue';

    const count = ref(0);

    function increment() {
      count.value++;
    }

    function decrement() {
      if (count.value > 0) {
        count.value--;
      }
    }

    function reset() {
      count.value = 0;
    }
</script>


<template>
    <div>
        <h1>Counter:  {{ count }}</h1>
        <div class="line-button">
            <button @click="increment" class="increment">Increment</button>
            <button @click="decrement" class="decrement">Decrement</button>
        </div>
        <div class="line-button">
            <button @click="reset" class="reset">Reset</button>
        </div>
    </div>
    <footer>
        <p>Created by Jonathan Stoff (JonathanStoff@ARETUM.com)</p>
    </footer>
</template>



<script>
export default {
    name: 'CounterComponent',
    props: {
        msg: String
    }
}
</script>
<style scoped>
    footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        background-color: #f8f9fa;
        padding: 10px 0;
    }
    .line-button{
        display: flex;
        justify-content: center;
    }
    h1 {
        font-size: 2rem;
        margin: 0;
        color: #002266;
    }
    .increment {
        background-color: #00cc99;
        color: white;
        font-weight: bold;
        padding-top: 0.5rem;
        padding-bottom: 0.5rem;
        padding-left: 1rem;
        padding-right: 1rem;
        margin: .5rem;
        border-radius: 0.25rem;
    }

    .increment:hover {
        background-color: #4dffd2;
    }
    .decrement {
        background-color: #ff0000;
        color: white;
        font-weight: bold;
        padding-top: 0.5rem;
        padding-bottom: 0.5rem;
        padding-left: 1rem;
        padding-right: 1rem;
        margin: .5rem;
        border-radius: 0.25rem;
    }

    .decrement:hover {
        background-color: #ff6666;
    }
    .reset {
        background-color: white;
        color: black;
        font-weight: bold;
        padding-top: 0.5rem;
        padding-bottom: 0.5rem;
        padding-left: 1rem;
        padding-right: 1rem;
        margin: .5rem;
        border-radius: 0.25rem;
    }

    .reset:hover {
        background-color: #e7e6e7;
    }
    h3 {
        margin: 40px 0 0;
    }
    ul {
        list-style-type: none;
        padding: 0;
    }
    li {
        display: inline-block;
        margin: 0 10px;
    }
    a {
        color: #42b983;
    }
</style>
