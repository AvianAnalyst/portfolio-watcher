<template>
    <div class="report">
        <input v-model="date" @change="sendUpDate" type="date"> <p>{{date}}</p>
    </div>
</template>

<script>
    export default {
        name: "report",
        data(){
            return {
                date: null,
            };
        },
        methods: {
            sendUpDate() {
                this.$emit('change', this.date);
                // eslint-disable-next-line no-console
                console.log(this.date);
            }
        },
    };
</script>

<style>
    .report {
        text-align: center;
    }
</style>
