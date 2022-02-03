<script>
import { HorizontalBar, mixins } from 'vue-chartjs';
import ChartJSPluginDatalabels from 'chartjs-plugin-datalabels';

export default {
  extends: HorizontalBar,
  mixins: [mixins.reactiveProp],

  name: 'GuessesChart',

  data: () => ({
    options: {
      indexAxis: 'y',
      responsive: true,
      maintainAspectRatio: false,
      legend: {
        display: false,
      },
      tooltips: {
        enabled: false,
      },
      scales: {
        xAxes: [{
          gridLines: {
            display: false,
          },
          ticks: {
            display: false,
            beginAtZero: true,
          },
        }],
        yAxes: [{
          gridLines: {
            display: false,
          },
        }],
      },
      plugins: {
        datalabels: {
          color: 'white',
          display: true,
        },
      },
    },
  }),

  props: {
    // chartData: Array,
  },

  mounted() {
    this.addPlugin(ChartJSPluginDatalabels);
    this.renderChart(this.chartData, this.options);
  },
};
</script>

<style scoped>

</style>
